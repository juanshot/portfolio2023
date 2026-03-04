<script setup lang="ts">
const { tm, rt } = useI18n();
</script>

<template>
  <div id="experience" class="py-24 sm:py-32 bg-[#09090b]">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:mx-0">
        <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-cyan-300 inline-block">
          {{ $t('experience.title') }}
        </h2>
      </div>
      <div class="mx-auto mt-16 max-w-2xl lg:mx-0 lg:max-w-none">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <div v-for="(item, index) in tm('experience.items')" :key="index" class="relative pl-8 border-l border-zinc-800 hover:border-blue-500 transition-colors duration-300 group">
            <div class="absolute top-0 left-[-5px] h-2.5 w-2.5 rounded-full bg-blue-500 ring-4 ring-[#09090b] group-hover:bg-cyan-400 transition-colors"></div>
            <time class="block text-sm leading-6 text-zinc-500">{{ rt(item.period) }}</time>
            <h3 class="mt-2 text-lg font-semibold leading-8 text-white group-hover:text-blue-400 transition-colors">
              {{ rt(item.role) }}
            </h3>
            <p class="text-base leading-7 text-zinc-400">{{ rt(item.company) }}</p>
            <div class="mt-4 flex flex-wrap gap-2">
              <span v-for="skill in item.skills" :key="skill" class="inline-flex items-center rounded-md bg-blue-400/10 px-2 py-1 text-xs font-medium text-blue-400 ring-1 ring-inset ring-blue-400/20">
                {{ rt(skill) }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
