<template>
  <div>
    <!-- Add a header or any common components here -->
    <header class="bg-slate-50 text-white py-4">
      <nav class="container mx-auto px-4">
        <ul class="flex space-x-4"></ul>
      </nav>
    </header>

    <!-- The main content area where pages are rendered -->
    <main class="container mx-auto px-4 py-6">
      <NuxtPage />
    </main>

    <!-- Add a footer here if needed -->
    <footer class="bg-gray-800 text-white py-4 mt-12 text-center">
      © 2024 Juan Garcia. All rights reserved.
    </footer>
  </div>
</template>
