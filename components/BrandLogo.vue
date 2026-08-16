<script setup lang="ts">
withDefaults(
  defineProps<{
    variant?: "inline" | "stacked" | "mark";
    height?: number;
  }>(),
  { variant: "inline", height: 32 },
);

const SOURCES = {
  inline: { src: "/brand/logo-inline.svg", ratio: 394 / 52 },
  stacked: { src: "/brand/logo-stacked.svg", ratio: 332 / 104 },
  mark: { src: "/brand/mark.svg", ratio: 1 },
} as const;
</script>

<template>
  <img
    :src="SOURCES[variant].src"
    :height="height"
    :width="Math.round(height * SOURCES[variant].ratio)"
    alt="Garcia Solutions"
    decoding="async"
  />
</template>
