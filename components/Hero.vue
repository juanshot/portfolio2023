<script setup lang="ts">
const isCalOpen = useState('isCalOpen');

const openCal = () => {
  if (isCalOpen.value !== undefined) {
    isCalOpen.value = true;
  }
};
</script>

<template>
  <div class="relative overflow-hidden py-24 sm:py-32 bg-[#09090b]">
    <div class="mx-auto max-w-7xl px-6 lg:px-8 relative z-10">
      <div class="mx-auto max-w-2xl lg:max-w-none">
        <div class="text-center lg:text-left">
          <h1 class="text-4xl font-bold tracking-tight text-white sm:text-6xl md:text-8xl font-mono">
            <span class="block text-transparent bg-clip-text bg-gradient-to-r from-blue-500 via-cyan-400 to-blue-600 pb-2">
              {{ $t('hero.title') }}
            </span>
          </h1>
          <p class="mt-6 text-lg leading-8 text-zinc-400 max-w-2xl">
            {{ $t('hero.intro') }}
          </p>
          <div class="mt-10 flex items-center justify-center lg:justify-start gap-x-6">
            <button @click="openCal" class="rounded-md bg-blue-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 transition-all duration-300">
              {{ $t('hero.cta') }}
            </button>
            <a href="#about" class="text-sm font-semibold leading-6 text-white hover:text-blue-400 transition-colors">
              {{ $t('about.title') }} <span aria-hidden="true">→</span>
            </a>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Background Gradient Blob -->
    <div class="absolute top-0 right-0 -z-10 transform-gpu overflow-hidden blur-3xl" aria-hidden="true">
      <div class="relative left-[calc(50%+3rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 bg-gradient-to-tr from-[#3b82f6] to-[#06b6d4] opacity-20 sm:left-[calc(50%+36rem)] sm:w-[72.1875rem]" style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)"></div>
    </div>
  </div>
</template>
