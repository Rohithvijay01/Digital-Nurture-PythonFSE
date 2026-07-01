
"""
1. THE REQUEST-RESPONSE CYCLE (GET /api/courses/)
   - Browser initiates an HTTP GET request to /api/courses/.
   - WSGI/ASGI Server catches the raw network request and parses it into a Django HttpRequest object.
   - Middleware Pipeline processes the request sequentially (checking security, sessions, etc.).
   - URL Router (urls.py) scans the path and matches it to the assigned view function/class.
   - View contains the business logic. It queries the database using the Model ORM.
   - Model returns database records, which the View structures into data (or JSON).
   - View returns a Django HttpResponse object.
   - Middleware Pipeline processes the response on its way back out.
   - Browser receives the HTTP response and renders it for the user.

2. MIDDLEWARE SITUATION AND CLASSES
   Middleware acts as a global security guard/interceptor sitting between the server gateway and the URL router.
   Two built-in Django middleware classes:
   - django.middleware.security.SecurityMiddleware: Handles standard production security enhancements 
     like XSS filter headers, SSL redirects, and content-type sniffing protection.
   - django.middleware.csrf.CsrfViewMiddleware: Protects POST/PUT/DELETE forms from Cross-Site Request 
     Forgery by verifying unique security tokens on unsafe requests.

3. WSGI VS ASGI
   - WSGI (Web Server Gateway Interface): The traditional Python synchronous standard. It handles requests 
     in a single-threaded blocking loop (one worker handles one request at a time). Django uses this by default.
   - ASGI (Asynchronous Server Gateway Interface): The modern successor that supports asynchronous capabilities. 
     It handles long-lived connections natively without blocking execution lines.
   - When to switch? You switch to ASGI when your system needs real-time connections like WebSockets, 
     long-polling, or HTTP/2 multiplexing.

4. MVC TO MVT MAPPING
   Traditional MVC (Model-View-Controller) maps directly to Django's MVT (Model-View-Template) pattern:
   - Model (MVC)     --->  Model (MVT): Maps database structures cleanly to Python objects.
   - View (MVC)      --->  Template (MVT): The presentation layer that handles what the user visually sees.
   - Controller (MVC)--->  View (MVT): The engine/brain where requests are parsed and logic is processed.
"""