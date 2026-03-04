<script setup lang="ts">
const isCalOpen = useState('isCalOpen', () => false);

const openCal = () => {
  isCalOpen.value = true;
};

const closeCal = () => {
  isCalOpen.value = false;
};

onMounted(() => {
  (function (C, A, L) {
    let p = function (a, ar) { a.q.push(ar); };
    let d = C.document;
    C.Cal = C.Cal || function () {
      let cal = C.Cal;
      let ar = arguments;
      if (!cal.loaded) {
        cal.ns = {};
        cal.q = cal.q || [];
        d.head.appendChild(d.createElement("script")).src = A;
        cal.loaded = true;
      }
      if (ar[0] === L) {
        const api = function () { p(api, arguments); };
        const namespace = ar[1];
        api.q = api.q || [];
        typeof namespace === "string" ? (cal.ns[namespace] = api) && p(api, ar) : p(cal, ar);
        return;
      }
      p(cal, ar);
    };
  })(window, "https://app.cal.com/embed/embed.js", "init");

  Cal("init", { origin: "https://cal.com" });

  Cal("ui", { "styles": { "branding": { "brandColor": "#3b82f6" } }, "hideEventTypeDetails": false, "layout": "month_view" });
});
</script>

<template>
  <div id="contact" class="py-24 sm:py-32 bg-[#09090b]">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:mx-0">
        <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-cyan-300 inline-block">
          {{ $t('contact.title') }}
        </h2>
        <p class="mt-6 text-lg leading-8 text-zinc-400">
          {{ $t('contact.description') }}
        </p>
        <div class="mt-8 flex flex-col gap-4 text-zinc-300">
          <div class="flex items-center gap-3">
            <svg class="h-6 w-6 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            <a :href="'mailto:' + $t('contact.email')" class="hover:text-blue-400 transition-colors">{{ $t('contact.email') }}</a>
          </div>
          <div class="flex items-center gap-3">
            <svg class="h-6 w-6 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
            </svg>
            <span>{{ $t('contact.phone') }}</span>
          </div>
          <div class="flex items-center gap-3">
            <svg class="h-6 w-6 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            <span>{{ $t('contact.address') }}</span>
          </div>
        </div>

        <div class="mt-10">
          <button @click="openCal" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-full text-base font-bold transition-colors shadow-lg shadow-blue-500/20 flex items-center gap-2">
            <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
            {{ $t('hero.cta') }}
          </button>
        </div>
      </div>
    </div>

    <!-- Cal.com Modal -->
    <Transition
      enter-active-class="transition ease-out duration-300"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition ease-in duration-200"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div v-if="isCalOpen" class="fixed inset-0 z-[100] flex items-center justify-center p-4 sm:p-6">
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-black/80 backdrop-blur-sm" @click="closeCal"></div>
        
        <!-- Modal Content -->
        <div class="relative w-full max-w-5xl bg-[#09090b] rounded-2xl shadow-2xl border border-zinc-800 overflow-hidden h-[85vh] sm:h-[80vh]">
          <button @click="closeCal" class="absolute top-4 right-4 z-10 p-2 bg-zinc-800/50 hover:bg-zinc-700 rounded-full text-zinc-400 hover:text-white transition-colors">
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          
          <div class="w-full h-full bg-zinc-900/50">
            <iframe 
              src="https://cal.com/juan-garcia-jtr2lv" 
              class="w-full h-full border-none"
              frameborder="0"
              allow="camera; microphone; autoplay; fullscreen"
            ></iframe>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>
