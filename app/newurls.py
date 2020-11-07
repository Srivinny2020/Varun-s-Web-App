from django.urls import path
from .views import Index, worldnews

urlpatterns = [
    path('', Index, name='Index'),
    path('wn/', wn, name='WorldNews')

]
