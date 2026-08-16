#!/usr/bin/env python3
"""Rasteriza los SVG de marca a PNG/ICO para favicon, apple-touch-icon y OG.

Por que un rasterizador propio: en este Mac no hay ImageMagick ni librsvg, y las
dos rutas de Python (cairosvg, reportlab/renderPM) dependen de libcairo nativo,
que tampoco esta. `qlmanage` no genera thumbnail para SVG. Los paths de marca
usan solo M/Q/V/H/L/Z y son poligonos cerrados, asi que aplanar las cuadraticas
y rellenar con Pillow alcanza y no agrega dependencias.

Los contornos interiores (el hueco de la "a", el punto de la "i") vienen como
subpaths adicionales dentro del mismo `d`, asi que se combinan por XOR, que es
la regla even-odd que usa SVG por defecto.

Uso:
    python3 scripts/rasterize.py
"""

import re
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
BRAND = ROOT / "public" / "brand"
PUBLIC = ROOT / "public"

SS = 4  # supersampling para antialiasing
BG = (9, 9, 11)
GRAD = ((59, 130, 246), (34, 211, 238))  # blue-500 -> cyan-400
MONO = "/System/Library/Fonts/Menlo.ttc"

TOKEN = re.compile(r"([MQVHLZmqvhlz])|(-?\d*\.?\d+(?:e-?\d+)?)")


def parse_path(d: str) -> list[list[tuple[float, float]]]:
    """Aplana un atributo `d` a una lista de subpaths de puntos."""
    items = [(c, n) for c, n in TOKEN.findall(d)]
    subpaths: list[list[tuple[float, float]]] = []
    pts: list[tuple[float, float]] = []
    x = y = 0.0
    i = 0
    cmd = None

    def nums(k: int) -> list[float]:
        nonlocal i
        out = []
        while len(out) < k:
            c, n = items[i]
            i += 1
            if n:
                out.append(float(n))
        return out

    while i < len(items):
        c, n = items[i]
        if c:
            cmd = c
            i += 1
            if cmd in "Zz":
                if pts:
                    subpaths.append(pts)
                    pts = []
                continue
        if cmd in "Mm":
            if pts:
                subpaths.append(pts)
                pts = []
            x, y = nums(2)
            pts.append((x, y))
            cmd = "L"  # coordenadas sueltas tras M son lineto
        elif cmd == "L":
            x, y = nums(2)
            pts.append((x, y))
        elif cmd == "H":
            (x,) = nums(1)
            pts.append((x, y))
        elif cmd == "V":
            (y,) = nums(1)
            pts.append((x, y))
        elif cmd == "Q":
            x1, y1, x2, y2 = nums(4)
            # 12 segmentos por curva: a 4x supersampling la faceta es invisible
            for t in (s / 12 for s in range(1, 13)):
                u = 1 - t
                pts.append(
                    (u * u * x + 2 * u * t * x1 + t * t * x2,
                     u * u * y + 2 * u * t * y1 + t * t * y2)
                )
            x, y = x2, y2
        else:
            i += 1
    if pts:
        subpaths.append(pts)
    return subpaths


def path_mask(d: str, size: tuple[int, int], sx: float, sy: float,
              ox: float, oy: float) -> Image.Image:
    """Mascara del path, combinando subpaths por even-odd (XOR)."""
    total = Image.new("L", size, 0)
    for sub in parse_path(d):
        if len(sub) < 3:
            continue
        layer = Image.new("L", size, 0)
        ImageDraw.Draw(layer).polygon(
            [((px - ox) * sx, (py - oy) * sy) for px, py in sub], fill=255
        )
        # difference == XOR para mascaras binarias 0/255
        total = ImageChops.difference(total, layer)
    return total


def gradient(size: tuple[int, int]) -> Image.Image:
    """Gradiente diagonal, equivalente al linearGradient x1,y1 -> x2,y2 del SVG."""
    w, h = size
    tx = np.linspace(0.0, 1.0, w)[None, :]
    ty = np.linspace(0.0, 1.0, h)[:, None]
    t = ((tx + ty) / 2)[:, :, None]
    c0 = np.array(GRAD[0], float)
    c1 = np.array(GRAD[1], float)
    return Image.fromarray((c0 + (c1 - c0) * t).astype(np.uint8), mode="RGB")


def render(svg_path: Path, out_w: int) -> Image.Image:
    """Renderiza un SVG de marca a RGBA respetando fills planos y el gradiente."""
    tree = ET.parse(svg_path)
    root = tree.getroot()
    ox, oy, vw, vh = (float(v) for v in root.get("viewBox").split())
    out_h = round(out_w * vh / vw)
    w, h = out_w * SS, out_h * SS
    sx, sy = w / vw, h / vh

    canvas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ns = "{http://www.w3.org/2000/svg}"

    rect = root.find(f"{ns}rect")
    if rect is not None:
        rx = float(rect.get("rx", 0)) * sx
        ImageDraw.Draw(canvas).rounded_rectangle(
            [0, 0, w - 1, h - 1], radius=rx, fill=rect.get("fill", "#000000")
        )

    for el in root.iter(f"{ns}path"):
        fill = el.get("fill", "#000000")
        mask = path_mask(el.get("d"), (w, h), sx, sy, ox, oy)
        if fill.startswith("url("):
            # El browser usa gradientUnits="objectBoundingBox" por defecto, o sea
            # cada path recibe el gradiente completo. Replicarlo por bbox evita
            # que las llaves salgan casi monocromas en el PNG.
            box = mask.getbbox()
            if box is None:
                continue
            bw, bh = box[2] - box[0], box[3] - box[1]
            layer = Image.new("RGB", (w, h))
            layer.paste(gradient((bw, bh)), (box[0], box[1]))
            canvas.paste(layer, (0, 0), mask)
        else:
            canvas.paste(Image.new("RGBA", (w, h), fill), (0, 0), mask)

    return canvas.resize((out_w, out_h), Image.LANCZOS)


def main() -> int:
    mark = render(BRAND / "mark.svg", 512)
    mark.save(PUBLIC / "apple-touch-icon.png")
    Image.alpha_composite(
        Image.new("RGBA", mark.size, BG + (255,)), mark
    ).convert("RGB").resize((180, 180), Image.LANCZOS).save(
        PUBLIC / "apple-touch-icon.png"
    )

    ico = Image.alpha_composite(Image.new("RGBA", mark.size, BG + (255,)), mark)
    ico.save(PUBLIC / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

    # OG: fondo oscuro + lockup apilado centrado + tagline
    og = Image.new("RGB", (1200, 630), BG)
    lockup = render(BRAND / "logo-stacked.svg", 620)
    og.paste(lockup, ((1200 - lockup.width) // 2, 170), lockup)
    draw = ImageDraw.Draw(og)
    font = ImageFont.truetype(MONO, 30)
    tagline = "Build  //  Lead  //  Teach"
    tw = draw.textbbox((0, 0), tagline, font=font)[2]
    draw.text(((1200 - tw) // 2, 420), tagline, font=font, fill=(161, 161, 170))
    og.save(PUBLIC / "og-image.png", optimize=True)

    for p in ("apple-touch-icon.png", "favicon.ico", "og-image.png"):
        f = PUBLIC / p
        print(f"escrito : {f}  ({f.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
