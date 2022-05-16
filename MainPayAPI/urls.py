from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', payInfo, name = 'landing'),
    path('checkout_session/<int:pk>', stripePost, name = 'checkout_session'),
    path('webhook/stripe/', stripe_webhook, name = 'stripe_webhook'),
    path('success/', successReq, name = 'success'),
    path('cancel/', cancelReq, name = 'cancel'),
]
