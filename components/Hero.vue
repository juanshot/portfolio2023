<script setup lang="ts">
const { open } = useCal();
const { tm, rt } = useI18n();

const words = computed(() => tm('hero.words').map((w: unknown) => rt(w as string)));
</script>

<template>
  <section class="relative overflow-hidden bg-dark-bg">
    <div class="mx-auto max-w-7xl px-6 lg:px-8 relative z-10">
      <div
        class="grid items-center gap-12 py-20 sm:py-24 lg:grid-cols-2 lg:gap-8 lg:py-28"
      >
        <div class="text-center lg:text-left">
          <p
            class="mb-5 font-mono text-sm uppercase tracking-[0.2em] text-zinc-500"
          >
            {{ $t('hero.role') }}
          </p>
          <h1
            class="font-mono font-bold tracking-tight text-white text-5xl sm:text-7xl xl:text-8xl"
          >
            <span class="inline-flex items-start gap-6">
              <span class="flex flex-col">
                <span
                  v-for="word in words"
                  :key="word"
                  class="block bg-gradient-to-r from-blue-500 via-cyan-400 to-blue-600 bg-clip-text text-transparent pb-1"
                >
                  {{ word }}
                </span>
              </span>
              <span
                class="hidden sm:flex flex-col leading-none select-none bg-gradient-to-b from-blue-500 to-cyan-400 bg-clip-text text-transparent"
                aria-hidden="true"
              >
                <span>//</span>
                <span>//</span>
              </span>
            </span>
          </h1>

          <p class="mt-8 text-lg leading-8 text-zinc-400 max-w-xl mx-auto lg:mx-0">
            {{ $t('hero.intro') }}
          </p>
          <p class="mt-4 text-lg leading-8 text-zinc-400 max-w-xl mx-auto lg:mx-0">
            {{ $t('hero.expertise') }}
          </p>

          <div
            class="mt-10 flex flex-wrap items-center justify-center lg:justify-start gap-4"
          >
            <button
              type="button"
              class="rounded-md bg-gradient-to-r from-blue-600 to-cyan-500 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-blue-500/25 hover:from-blue-500 hover:to-cyan-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-500 transition-all duration-300"
              @click="open"
            >
              {{ $t('hero.cta') }}
            </button>
            <a
              href="#about"
              class="rounded-md border border-zinc-700 px-5 py-3 text-sm font-semibold text-white hover:border-blue-500 hover:text-blue-400 transition-colors"
            >
              {{ $t('about.title') }} <span aria-hidden="true">→</span>
            </a>
          </div>
        </div>

        <div class="relative flex justify-center lg:justify-end">
          <!-- Glow detras del recorte: da profundidad y hace que el brillo real
               de la manga se lea como luz de borde y no como resto del recorte. -->
          <div
            class="absolute inset-0 -z-10 flex items-center justify-center"
            aria-hidden="true"
          >
            <div
              class="h-80 w-80 sm:h-[26rem] sm:w-[26rem] rounded-full bg-blue-500/25 blur-3xl"
            />
          </div>
          <!-- El fade inferior evita el corte plano del encuadre original, donde
               la camisa llega al borde de la foto. -->
          <img
            src="/images/juan.webp"
            width="479"
            height="680"
            alt="Juan Garcia"
            fetchpriority="high"
            decoding="async"
            class="w-full max-w-[280px] sm:max-w-[360px] lg:max-w-[440px] object-bottom [mask-image:linear-gradient(to_bottom,black_78%,transparent_100%)]"
          />
        </div>
      </div>
    </div>

    <div
      class="absolute top-0 right-0 -z-10 transform-gpu overflow-hidden blur-3xl"
      aria-hidden="true"
    >
      <div
        class="relative left-[calc(50%+3rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 bg-gradient-to-tr from-[#3b82f6] to-[#06b6d4] opacity-20 sm:left-[calc(50%+36rem)] sm:w-[72.1875rem]"
        style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)"
      />
    </div>
  </section>
</template>
