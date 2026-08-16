<script setup lang="ts">
const { locale, locales } = useI18n();
const switchLocalePath = useSwitchLocalePath();
const localePath = useLocalePath();
const route = useRoute();

const isMenuOpen = ref(false);

const availableLocales = computed(() =>
  locales.value.filter((i) => i.code !== locale.value),
);

const sections = [
  { hash: "#about", label: "about.title" },
  { hash: "#experience", label: "experience.title" },
  { hash: "#skills", label: "skills.title" },
];

watch(
  () => route.fullPath,
  () => (isMenuOpen.value = false),
);
</script>

<template>
  <nav
    class="fixed top-0 w-full z-50 bg-dark-bg/80 backdrop-blur-md border-b border-dark-border"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <NuxtLink
          :to="localePath('/')"
          class="flex items-center hover:opacity-80 transition-opacity"
        >
          <BrandLogo variant="mark" :height="32" class="sm:hidden rounded-md" />
          <BrandLogo variant="inline" :height="28" class="hidden sm:block" />
        </NuxtLink>

        <div class="hidden md:flex items-baseline space-x-4">
          <NuxtLink
            v-for="section in sections"
            :key="section.hash"
            :to="localePath('/') + section.hash"
            class="text-zinc-400 hover:text-blue-400 px-3 py-2 rounded-md text-sm font-medium transition-colors"
          >
            {{ $t(section.label) }}
          </NuxtLink>
          <NuxtLink
            :to="localePath('/') + '#contact'"
            class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-full text-sm font-bold transition-colors shadow-lg shadow-blue-500/20"
          >
            {{ $t("contact.title") }}
          </NuxtLink>
        </div>

        <div class="flex items-center gap-2">
          <NuxtLink
            v-for="loc in availableLocales"
            :key="loc.code"
            :to="switchLocalePath(loc.code)"
            class="text-zinc-400 hover:text-white text-sm font-medium uppercase transition-colors border border-dark-border rounded px-2 py-1 hover:border-zinc-600"
          >
            {{ loc.code }}
          </NuxtLink>

          <button
            type="button"
            class="md:hidden inline-flex items-center justify-center p-2 rounded-md text-zinc-400 hover:text-white hover:bg-dark-surface transition-colors"
            :aria-expanded="isMenuOpen"
            aria-controls="mobile-menu"
            :aria-label="isMenuOpen ? 'Close menu' : 'Open menu'"
            @click="isMenuOpen = !isMenuOpen"
          >
            <svg
              class="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.75"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                :d="
                  isMenuOpen
                    ? 'M6 18L18 6M6 6l12 12'
                    : 'M3.75 6.75h16.5M3.75 12h16.5M3.75 17.25h16.5'
                "
              />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <Transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0 -translate-y-2"
      leave-active-class="transition duration-150 ease-in"
      leave-to-class="opacity-0 -translate-y-2"
    >
      <div
        v-if="isMenuOpen"
        id="mobile-menu"
        class="md:hidden border-t border-dark-border bg-dark-bg/95 backdrop-blur-md"
      >
        <div class="px-4 py-3 space-y-1">
          <NuxtLink
            v-for="section in sections"
            :key="section.hash"
            :to="localePath('/') + section.hash"
            class="block px-3 py-2 rounded-md text-base font-medium text-zinc-300 hover:text-blue-400 hover:bg-dark-surface transition-colors"
          >
            {{ $t(section.label) }}
          </NuxtLink>
          <NuxtLink
            :to="localePath('/') + '#contact'"
            class="block px-3 py-2 rounded-md text-base font-bold text-white bg-blue-600 hover:bg-blue-700 transition-colors text-center mt-2"
          >
            {{ $t("contact.title") }}
          </NuxtLink>
        </div>
      </div>
    </Transition>
  </nav>
</template>
