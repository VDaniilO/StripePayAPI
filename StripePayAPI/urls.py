from django.contrib import admin
from django.urls import path, include

from MainPayAPI.views import PayAPIUpdate, PayAPIList, stripePost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('MainPayAPI.urls')),
    path('api/v1/buy', PayAPIList.as_view()),
    path('api/v1/buy/<int:pk>', PayAPIUpdate.as_view()),
]
