const CACHE_NAME = 'nelson-gpt-cache-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/manifest.json',
  '/logo192.png',
  '/logo512.png'
  // Add other static assets like CSS, JS files if they exist and need caching
];

// Install event: Cache core assets
self.addEventListener('install', event => {
  console.log('[ServiceWorker] Install');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('[ServiceWorker] Caching app shell');
        return cache.addAll(urlsToCache);
      })
      .catch(error => {
        console.error('[ServiceWorker] Failed to cache app shell:', error);
      })
  );
});

// Activate event: Clean up old caches
self.addEventListener('activate', event => {
  console.log('[ServiceWorker] Activate');
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            console.log('[ServiceWorker] Removing old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  return self.clients.claim();
});

// Fetch event: Serve cached content or fetch from network
self.addEventListener('fetch', event => {
  console.log('[ServiceWorker] Fetch event for ', event.request.url);
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          console.log('[ServiceWorker] Found in cache:', event.request.url);
          return response;
        }
        console.log('[ServiceWorker] Network request for ', event.request.url);
        return fetch(event.request);
      })
      .catch(error => {
        console.error('[ServiceWorker] Error fetching data:', error);
        // Optional: Respond with a fallback page if offline
        // return caches.match('/offline.html');
      })
  );
});
