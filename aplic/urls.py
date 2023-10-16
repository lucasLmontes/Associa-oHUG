from django.urls import path
from aplic.views import index

urlpatterns = [
    path('', index, name='index.html'),
]
