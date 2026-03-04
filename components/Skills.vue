<script setup lang="ts">
const { tm, rt } = useI18n();
</script>

<template>
  <div id="skills" class="py-24 sm:py-32 bg-[#09090b]">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:mx-0">
        <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-cyan-300 inline-block">
          {{ $t('skills.title') }}
        </h2>
        <p class="mt-6 text-lg leading-8 text-zinc-400">
          {{ $t('skills.description') }}
        </p>
      </div>
      <div class="mx-auto mt-16 max-w-2xl lg:mx-0 lg:max-w-none">
        <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3">
          <div v-for="(skill, index) in tm('skills.list')" :key="index" class="flex flex-col group hover:-translate-y-2 transition-transform duration-300">
            <dt class="text-base font-semibold leading-7 text-white">
              <div class="mb-6 flex h-10 w-10 items-center justify-center rounded-lg bg-blue-500 group-hover:bg-cyan-500 transition-colors">
                <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 6.75L22.5 12l-5.25 5.25m-10.5 0L1.5 12l5.25-5.25m7.5-3l-4.5 18" />
                </svg>
              </div>
              <span class="group-hover:text-cyan-300 transition-colors">{{ rt(skill) }}</span>
            </dt>
          </div>
        </dl>
      </div>
    </div>
  </div>
</template>
