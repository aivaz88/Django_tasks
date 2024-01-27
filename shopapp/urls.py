from django.urls import path
from .views import main, about, contacts, login_form, registration_form, greeting, clothes, shoes, accessories
from.views import item_card, order_access

urlpatterns = [
    path('', main, name='main'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('login/', login_form, name='login_form'),
    path('registration/', registration_form, name='registration'),
    path('greeting/', greeting, name='greeting'),
    path('clothes/', clothes, name='clothes'),
    path('shoes/', shoes, name='shoes'),
    path('accessories/', accessories, name='accessories'),
    path('item_card/<str:pk>/', item_card, name='item_card'),
    path('order_access/<int:pk>/', order_access, name='order_access')
]
