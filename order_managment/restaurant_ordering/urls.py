from django.urls import path

from .import views

app_name = "restaurant_ordering"

urlpatterns = [
    path('cooking_list/', views.cooking_list, name='cooking_list'), #http://127.0.0.1:8000/worksite/cooking_list/
    path('delivery_list/', views.delivery_list, name='delivery_list'), #http://127.0.0.1:8000/worksite/delivery_list/
    path('payment_status/', views.payment_status_update, name='payment_status'), #Перенаправляется на http://127.0.0.1:8000/worksite/delivery_list/

]
