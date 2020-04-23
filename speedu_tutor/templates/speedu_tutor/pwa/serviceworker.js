var CACHE_NAME = 'speedu-cache';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll([
        '/offline'
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
    // CODELAB: Add fetch event handler here.
    if (event.request.mode !== 'navigate') {
        // Not a page navigation, bail.
        return;
    }
    event.respondWith(
        fetch(event.request)
            .catch(() => {
            return caches.open(CACHE_NAME)
                .then((cache) => {
                    return cache.match('/offline');
                });
            })
    );
});