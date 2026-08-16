<template>
  <section id="skills" class="py-24 bg-dark-bg">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:mx-0">
        <h2
          class="text-3xl font-bold tracking-tight sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-cyan-300 inline-block"
        >
          {{ $t("skills.title") }}
        </h2>
        <p class="mt-6 text-lg leading-8 text-zinc-400">
          {{ $t("skills.description") }}
        </p>
      </div>

      <div class="mt-16 grid items-start gap-8 sm:grid-cols-2 lg:grid-cols-3">
        <div
          v-for="group in skillGroups"
          :key="group.key"
          class="rounded-xl border border-dark-border bg-dark-surface/40 p-6 hover:border-zinc-700 transition-colors"
        >
          <h3
            class="text-sm font-semibold uppercase tracking-wider text-zinc-500"
          >
            {{ $t(`skills.groups.${group.key}`) }}
          </h3>
          <ul class="mt-5 flex flex-wrap gap-x-6 gap-y-5">
            <li
              v-for="tech in group.items"
              :key="tech.name"
              class="group flex w-16 flex-col items-center gap-2 text-center"
              :title="tech.name"
            >
              <Icon
                :name="tech.icon"
                class="h-8 w-8 text-zinc-500 group-hover:text-white transition-colors duration-300"
                aria-hidden="true"
              />
              <span
                class="text-[11px] leading-tight text-zinc-600 group-hover:text-zinc-300 transition-colors duration-300"
              >
                {{ tech.name }}
              </span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>
