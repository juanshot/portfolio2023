<script setup lang="ts">
const { tm, rt } = useI18n();

const certificates = computed(() =>
  tm("credentials.certificates").map((c: unknown) => rt(c as string)),
);
const languages = computed(() =>
  tm("credentials.languages").map((l: unknown) => rt(l as string)),
);
</script>

<template>
  <section id="credentials" class="py-24 bg-dark-bg">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <h2
        class="text-3xl font-bold tracking-tight sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-cyan-300 inline-block"
      >
        {{ $t("credentials.title") }}
      </h2>

      <div class="mt-16 grid items-start gap-8 md:grid-cols-3">
        <div
          class="rounded-xl border border-dark-border bg-dark-surface/40 p-6"
        >
          <h3
            class="text-sm font-semibold uppercase tracking-wider text-zinc-500"
          >
            {{ $t("credentials.educationTitle") }}
          </h3>
          <p class="mt-5 text-base font-semibold text-white">
            {{ $t("credentials.education.degree") }}
          </p>
          <p class="mt-1 text-sm text-zinc-400">
            {{ $t("credentials.education.school") }}
          </p>
          <time class="mt-2 block text-sm text-zinc-500">
            {{ $t("credentials.education.period") }}
          </time>
        </div>

        <div
          class="rounded-xl border border-dark-border bg-dark-surface/40 p-6"
        >
          <h3
            class="text-sm font-semibold uppercase tracking-wider text-zinc-500"
          >
            {{ $t("credentials.certificatesTitle") }}
          </h3>
          <ul class="mt-5 space-y-3">
            <li
              v-for="cert in certificates"
              :key="cert"
              class="flex gap-3 text-sm leading-6 text-zinc-300"
            >
              <span
                class="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-blue-500"
              />
              {{ cert }}
            </li>
          </ul>
        </div>

        <div
          class="rounded-xl border border-dark-border bg-dark-surface/40 p-6"
        >
          <h3
            class="text-sm font-semibold uppercase tracking-wider text-zinc-500"
          >
            {{ $t("credentials.languagesTitle") }}
          </h3>
          <ul class="mt-5 flex flex-wrap gap-2">
            <li
              v-for="lang in languages"
              :key="lang"
              class="inline-flex items-center rounded-md bg-blue-400/10 px-2.5 py-1 text-xs font-medium text-blue-400 ring-1 ring-inset ring-blue-400/20"
            >
              {{ lang }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>
