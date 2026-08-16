#!/usr/bin/env python3
"""Recorta el fondo de la foto de perfil y la deja con transparencia.

El original es una foto de estudio sobre pared blanca (254,254,254 en los bordes).
Tres detalles que obligan a algo mas fino que un "todo lo claro es fondo":

1. El sujeto toca el borde superior e inferior del encuadre, asi que el fondo no
   es un unico anillo: hay que sembrar desde todos los pixeles del borde, no solo
   desde las cuatro esquinas.
2. El cuero cabelludo iluminado llega a 208 y el fondo a 254. Un umbral unico lo
   suficientemente bajo para comerse la sombra proyectada tambien se come un
   mordisco de la cabeza. Por eso el umbral varia por region: estricto arriba
   (piel clara), permisivo abajo (camisa azul oscura, que es donde cae la sombra).
3. El antialiasing del borde mezcla sujeto con blanco, dejando un halo claro al
   recortar. Se corrige con erosion + una pasada de descontaminacion que baja el
   alpha de los pixeles claros que quedan en el borde.

Uso:
    python3 scripts/cutout.py ~/Downloads/1709720266955.jpg
"""

import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter

# Umbral de "fondo" interpolado por fila: y<210 cabeza, y>260 cuerpo.
THRESHOLD_STOPS = ([0, 210, 260], [236, 236, 212])

# Descontaminacion: en una banda de este ancho hacia adentro del contorno, los
# pixeles claros pierden alpha proporcionalmente.
EDGE_BAND_PX = 6
SPILL_RANGE = (215, 250)  # opaco por debajo de 215, transparente arriba de 250

OUT_DIR = Path(__file__).resolve().parent.parent / "public" / "images"


def background_mask(channel_min: np.ndarray) -> np.ndarray:
    """True donde hay sujeto, False donde hay fondo conectado al borde."""
    h, w = channel_min.shape
    ys, vals = THRESHOLD_STOPS
    threshold = np.interp(np.arange(h), ys + [h], vals + [vals[-1]])[:, None]

    # OJO: ImageDraw.floodfill es un no-op silencioso sobre imagenes creadas con
    # Image.fromarray (el buffer numpy llega de solo lectura). El .copy() es
    # obligatorio, no cosmetico.
    flood = Image.fromarray(
        ((channel_min >= threshold) * 255).astype(np.uint8), mode="L"
    ).copy()

    # Sembrar desde todo el perimetro. floodfill retorna de inmediato si la
    # semilla ya tiene el color de relleno, asi que repetir sale barato.
    for x in range(w):
        for y in (0, h - 1):
            if flood.getpixel((x, y)) == 255:
                ImageDraw.floodfill(flood, (x, y), 128, thresh=0)
    for y in range(h):
        for x in (0, w - 1):
            if flood.getpixel((x, y)) == 255:
                ImageDraw.floodfill(flood, (x, y), 128, thresh=0)

    return np.array(flood) != 128


def decontaminate(alpha: np.ndarray, channel_min: np.ndarray) -> np.ndarray:
    """Baja el alpha de los pixeles claros que sobreviven en el borde."""
    solid = Image.fromarray((alpha > 128).astype(np.uint8) * 255, mode="L")
    inner = solid.filter(ImageFilter.MinFilter(2 * EDGE_BAND_PX + 1))
    band = (np.array(solid) > 128) & (np.array(inner) <= 128)

    lo, hi = SPILL_RANGE
    keep = np.clip((hi - channel_min) / (hi - lo), 0.0, 1.0)
    out = alpha.astype(float)
    out[band] *= keep[band]
    return out.astype(np.uint8)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1

    src = Path(sys.argv[1]).expanduser()
    if not src.exists():
        print(f"no existe: {src}")
        return 1

    rgb = Image.open(src).convert("RGB")
    r, g, b = rgb.split()
    channel_min = np.array(ImageChops.darker(ImageChops.darker(r, g), b)).astype(int)

    subject = background_mask(channel_min)

    alpha_img = Image.fromarray((subject * 255).astype(np.uint8), mode="L")
    alpha_img = alpha_img.filter(ImageFilter.MinFilter(3))
    alpha_img = alpha_img.filter(ImageFilter.GaussianBlur(0.7))
    alpha = decontaminate(np.array(alpha_img), channel_min)

    cutout = rgb.convert("RGBA")
    cutout.putalpha(Image.fromarray(alpha, mode="L"))
    bbox = Image.fromarray(alpha, mode="L").getbbox()
    if bbox:
        cutout = cutout.crop(bbox)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    png = OUT_DIR / "juan.png"
    webp = OUT_DIR / "juan.webp"
    cutout.save(png, optimize=True)
    cutout.save(webp, quality=90, method=6)

    final_alpha = np.array(cutout.getchannel("A"))
    final_rgb = np.array(cutout.convert("RGB"))
    fringe = int(((final_alpha > 200) & (final_rgb.min(axis=2) >= 225)).sum())
    print(f"tamano  : {cutout.width}x{cutout.height}")
    print(f"sujeto  : {100 * (final_alpha > 128).mean():.1f}% del recorte")
    print(f"fringe  : {fringe} px claros aun opacos")
    print(f"escrito : {png} ({png.stat().st_size // 1024} KB)")
    print(f"escrito : {webp} ({webp.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
