import stripe

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics

from .models import Item
from .serializers import ItemSerializers

stripe.api_key = settings.STRIPE_SECRET_KEY

def payInfo(request):
    outInfo = Item.objects.all()
    context = {
        'outInfo': outInfo,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'MainPayAPI/landing.html', context = context)

@csrf_exempt
def stripePost(request, pk):
    YOUR_DOMAIN = "http://127.0.0.1:8000"
    item_id_get = Item.objects.get(pk = pk)
    checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item_id_get.price,
                        'product_data':{
                            'name': item_id_get.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/main/success/',
            cancel_url=YOUR_DOMAIN + '/main/cancel/',
        )
    return JsonResponse({
        'id': checkout_session.id
    })

def successReq(request):
    return render(request, 'MainPayAPI/success.html')

def cancelReq(request):
    return render(request, 'MainPayAPI/cancel.html')

class PayAPIList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers


class PayAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

@csrf_exempt
def stripe_webhook(request):
    payload = request.body

    print(payload)

    return HttpResponse(status=200)
