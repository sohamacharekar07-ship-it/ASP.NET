/* =========================================================
   DOT.NET CORE & PWA PRACTICAL – VI

   QUESTION 1:
   Create a simple website for a College Information Portal
   and convert it into a Progressive Web Application.
========================================================= */


/* ===========================
   manifest.json
   (PWA Identity File)
=========================== */
{
  "name": "College Information Portal",
  "short_name": "College Portal",
  "start_url": "/",
  "display": "standalone",
  "icons": [
    {
      "src": "/icons/icon1.png",
      "sizes": "128x128",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/icon2.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any"
    }
  ]
}


/* ===========================
   index.cshtml (Home Page)
=========================== */
@{
    ViewData["Title"] = "Home Page";
}
<div class="text-center">
    <h1 class="display-4">College Information Portal</h1>
    <h1 class="display-4">Welcome</h1>
    <p>Learn about
      <a href="https://learn.microsoft.com/aspnet/core">
        ASP.NET Core
      </a>
    </p>
</div>


/* ===========================
   service-worker.js
   (Basic Service Worker)
=========================== */
self.addEventListener("install", e => {
    console.log("Service workers installed ");
});

self.addEventListener("fetch", e => {
    e.responseWith(fetch(e.request));
});


/* ===========================
   _Layout.cshtml
   (Link Manifest + Register SW)
=========================== */
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>@ViewData["Title"] - HTMLtoPWA</title>

    <!-- PWA Manifest -->
    <link rel="manifest" href="/manifest.json" />

    <link rel="stylesheet" href="~/lib/bootstrap/dist/css/bootstrap.min.css" />
</head>

<body>

    <!-- Navbar -->
    <nav>
        <a asp-controller="Home" asp-action="Index">Home</a>
    </nav>

    <!-- Main Content -->
    <div>
        @RenderBody()
    </div>

    <!-- Footer -->
    <footer>
        © 2026 - HTMLtoPWA
    </footer>

    <!-- Service Worker Registration -->
    <script>
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/service-worker.js');
        }
    </script>

</body>
</html>



/* =========================================================
   QUESTION 2:
   Create a PWA that displays a custom offline page
   when the user is not connected to the internet.
========================================================= */


/* ===========================
   offline.html
=========================== */
<!DOCTYPE html>
<html>
<head>
    <title>Offline</title>
</head>
<body style="text-align:center; margin-top:100px;">
    <h1>You are Offline</h1>
</body>
</html>


/* ===========================
   service-worker.js (Offline Support)
=========================== */
const CACHE = "v1";

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open("offline-cache").then(cache => {
            return cache.addAll([
                "/",
                "/offline.html"
            ]);
        })
    );
    console.log("Service Worker Installed");
});

self.addEventListener("fetch", event => {
    event.respondWith(
        fetch(event.request).catch(() => {
            return caches.match("/offline.html");
        })
    );
});
