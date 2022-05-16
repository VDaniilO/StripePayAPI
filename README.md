INSTALLATION
------------

Install framework to the use in this project:
    
    pip install Django
    pip install djangorestframework
    pip install stripe
    
QUICK START
-----------

Pass to the main directory and run server after run server open stripe.exe for webhook:
    
    cd StripePayAPI
    manage.py runserver
    stripe.exe listen --forward-to http://127.0.0.1:8000/main/webhook/stripe/
    open browse and open http://127.0.0.1:8000/main/
