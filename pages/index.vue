<script setup lang="ts">
// Page meta for SEO
useHead({
  title: 'Juan Garcia - Software Engineer',
  meta: [
    { name: 'description', content: 'Portfolio of Juan Garcia, a Lead Software Engineer specialized in Nuxt, Vue, and TypeScript.' }
  ],
  bodyAttrs: {
    class: 'bg-[#09090b]'
  }
})
</script>

<template>
  <div>
    <Hero />
    
    <div id="about" class="relative py-24 sm:py-32 bg-[#09090b] overflow-hidden">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:mx-0">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-cyan-300 inline-block">
            {{ $t('about.title') }}
          </h2>
          <p class="mt-6 text-lg leading-8 text-zinc-400">
            {{ $t('about.description') }}
          </p>
        </div>
      </div>
      
      <!-- Decorative element -->
      <div class="absolute left-[calc(50%-4rem)] top-10 -z-10 transform-gpu blur-3xl sm:left-[calc(50%-18rem)] lg:left-48 lg:top-[calc(50%-30rem)] xl:left-[calc(50%-24rem)]" aria-hidden="true">
        <div class="aspect-[1108/632] w-[69.25rem] bg-gradient-to-r from-[#80caff] to-[#4f46e5] opacity-20" style="clip-path: polygon(73.6% 51.7%, 91.7% 11.8%, 100% 46.4%, 97.4% 82.2%, 92.5% 84.9%, 75.7% 64%, 55.3% 47.5%, 46.5% 49.4%, 45% 62.9%, 50.3% 87.2%, 21.3% 64.1%, 0.1% 100%, 5.4% 51.1%, 21.4% 63.9%, 58.9% 0.2%, 73.6% 51.7%)"></div>
      </div>
    </div>

    <Skills />
    <Experience />
    <Calendar />
  </div>
</template>
