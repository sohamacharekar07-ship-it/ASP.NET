10. a. Create a PWA with a Web App Manifest file including:
App name
Icons
Start URL
Display mode
Implement Push Notifications in a PWA.
Steps:
1.	Create an ASP.NET Core Empty Web App named PushNotification.
2.	Create a wwwroot folder.
3.	Add manifest.json with app name, icons, start URL and display mode.
4.	Create icons folder and add icon1.png and icon2.png.
5.	Add index.html and link manifest.json.
6.	Add app.js for service worker registration and notifications.
7.	Add service-worker.js for service worker events.
8.	Configure Program.cs with UseDefaultFiles() and UseStaticFiles().
9.	Run the project, install the PWA and test the notification.
Code:
manifest.json : 
{
  "name": "My PWA Application (Soham Acharekar (T001)",
  "short_name": "MyPWA",
  "start_url": "/index.html",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#0d6efd",
  "icons": [
    {
      "src": "icons/icon1.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "icons/icon2.png",
      "sizes": "447x447",
      "type": "image/png"
    }
  ]
}
index.html :
<!DOCTYPE html>
<html>
<head>
    <title>My PWA</title>
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#0d6efd">
</head>
<body>
    <h1>My Progressive Web App (Soham Acharekar(T001)</h1>
    <button onclick="showNotification()">
        Show Notification
    </button>
    <script src="app.js"></script>
</body>
</html>
app.js : 
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('service-worker.js')
        .then(() => console.log('Service Worker Registered'));
}
function showNotification() {
    Notification.requestPermission().then(permission => {
        if (permission === 'granted') {
            navigator.serviceWorker.ready.then(registration => {
                registration.showNotification('PWA Notification', {
                    body: 'Push Notification Working Successfully!',
                    icon: 'icons/icon1.png'
                });
            });
        }
    });
}
service-worker.js : 
self.addEventListener('install', event => {
    console.log('Service Worker Installed');
});

self.addEventListener('activate', event => {
    console.log('Service Worker Activated');
});
Program.cs : 
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
app.UseDefaultFiles();
app.UseStaticFiles();
app.Run();
Output:
 
 
 
 
10.b.Develop an E-Commerce PWA with Product Listing and Offline Cart Functionality
Steps:
1.	Create an ASP.NET Core Empty Web App named ECommercePWA.
2.	Configure Program.cs using UseDefaultFiles() and UseStaticFiles().
3.	Create manifest.json inside the wwwroot folder.
4.	Create an icons folder and add icon1.png and icon2.png.
5.	Create index.html with product listing and cart section.
6.	Create app.js for service worker registration and offline cart functionality.
7.	Create service-worker.js for caching application files.
8.	Run the project and open the application in the browser.
9.	Add products to the cart and test offline functionality using Chrome DevTools → Network → Offline.
Code:
Program.cs:
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
app.UseDefaultFiles();
app.UseStaticFiles();
app.Run();
manifest.json:
{
  "name": "E-Commerce PWA",
  "short_name": "ShopPWA",
  "start_url": "/index.html",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#0d6efd",
  "icons": [
    {
      "src": "icons/icon1.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "icons/icon2.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
index.html:
<!DOCTYPE html>
<html>
<head>
    <title>E-Commerce PWA</title>
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#0d6efd">
    <style>
        body {
            font-family: Arial;
            margin: 20px;
        }
        .container {
            display: flex;
            gap: 30px;
        }
        .cart-section {
            width: 30%;
            border: 1px solid gray;
            padding: 15px;
            min-height: 300px;
        }
        .product-section {
            width: 70%;
        }
        .products {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
        }
        .product {
            border: 1px solid gray;
            padding: 10px;
            width: 200px;
        }

        button {
            padding: 5px 10px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>E-Commerce PWA (Soham Acharekar (T001))</h1>
    <div class="container">
        <!-- Cart Section -->
        <div class="cart-section">
            <h2>Cart Items</h2>
            <ul id="cartList"></ul>
        </div>
        <!-- Product Section -->
        <div class="product-section">
            <h2>Products</h2>
            <div class="products">
                <div class="product">
                    <h3>Laptop</h3>
                    <p>Price: ₹50000</p>
                    <button onclick="addToCart('Laptop')">
                        Add to Cart
                    </button>
                </div>
                <div class="product">
                    <h3>Mobile</h3>
                    <p>Price: ₹20000</p>
                    <button onclick="addToCart('Mobile')">
                        Add to Cart
                    </button>
                </div>
                <div class="product">
                    <h3>Headphones</h3>
                    <p>Price: ₹3000</p>
                    <button onclick="addToCart('Headphones')">
                        Add to Cart
                    </button>
                </div>
            </div>
        </div>
    </div>
    <script src="app.js"></script>
</body>
</html>
app.js:
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('service-worker.js')
        .then(() => console.log('Service Worker Registered'));
}
let cart = JSON.parse(localStorage.getItem('cart')) || [];
displayCart();
function addToCart(product) {
    cart.push(product);
    localStorage.setItem('cart', JSON.stringify(cart));
    displayCart();
}
function displayCart() {
    let cartList = document.getElementById('cartList');
    cartList.innerHTML = '';
    cart.forEach(item => {
        let li = document.createElement('li');
        li.textContent = item;
        cartList.appendChild(li);
    });
}
service-worker.js:
const CACHE_NAME = 'ecommerce-cache-v1';
const urlsToCache = [
    '/',
    '/index.html',
    '/app.js',
    '/manifest.json'
];
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                return cache.addAll(urlsToCache);
            })
    );
});
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
    );
});
Output:
 
Test Offline Functionality
 

