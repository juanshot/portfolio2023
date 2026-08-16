// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-04-03",
  devtools: { enabled: true },
  modules: ["@nuxtjs/i18n", "@nuxt/icon", "@nuxt/fonts"],
  css: ["~/assets/css/tailwind.css"],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  app: {
    head: {
      htmlAttrs: { lang: "en" },
      link: [
        { rel: "icon", type: "image/svg+xml", href: "/favicon.svg" },
        { rel: "alternate icon", href: "/favicon.ico" },
        { rel: "apple-touch-icon", href: "/apple-touch-icon.png" },
      ],
      meta: [
        { name: "theme-color", content: "#09090b" },
        { property: "og:type", content: "website" },
        { property: "og:image", content: "/og-image.png" },
        { name: "twitter:card", content: "summary_large_image" },
        { name: "twitter:image", content: "/og-image.png" },
      ],
    },
  },
  fonts: {
    families: [
      { name: "Inter", provider: "google" },
      { name: "JetBrains Mono", provider: "google" },
    ],
  },
  icon: {
    serverBundle: { collections: ["simple-icons"] },
  },
  i18n: {
    locales: [
      { code: "en", file: "en.json", name: "English" },
      { code: "de", file: "de.json", name: "Deutsch" },
    ],
    langDir: "locales",
    defaultLocale: "en",
    strategy: "prefix_except_default",
  },
});
