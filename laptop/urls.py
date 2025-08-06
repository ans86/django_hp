from django.urls import path
from .views import laptop

urlpatterns = [
    path('', laptop, name='laptop'),
]