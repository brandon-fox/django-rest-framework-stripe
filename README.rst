======================
django-rest-framework-stripe
======================

Django REST Framework wrapper of the payments Django app for Stripe

* Forked (https://github.com/pinax/django-stripe-payments) and wrapped with Django REST Framework.
* All the templates is gone
* Forked (https://github.com/categorilla/django-rest-framework-stripe) for renaming app.

Install
======================
* pip install -e git+https://github.com/brandon-fox/django-rest-framework-stripe.git#egg=drfstripe
* Add 'drfstripe' to INSTALLED_APPS
* **Add to urls.py:** ``url(r"^api/stripe/", include("drfstripe.api.urls"))``

Endpoints
======================
* current-user/ (GET)
* subscription/ (GET/POST)
* change-card/  (GET/POST)
* change-card-token/ (POST)
* charges/      (GET)
* invoices/     (GET)
* plans/        (GET)
* events/       (GET)
* webhook/      (POST)
* cancel/       (POST)

**ALL TEMPLATES AND AJAX VIEWS HAVE BEEN REMOVED, USE ADDED ENDPOINTS**

Documentation can be found at http://django-stripe-payments.readthedocs.org
