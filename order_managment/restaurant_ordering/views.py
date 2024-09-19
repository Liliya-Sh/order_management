"""
Представления для приложения restaurant_ordering.
"""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .decorators import is_cook_decorator, is_delivery_decorator
from .models import Order, OrderItem


@login_required
@is_cook_decorator
def cooking_list(request):
    """ Получаем все заказы, которые необходимо приготовить.
         Меняем статус заказа с False на True и наоборот(Готовится/Готов)."""
    orders = Order.objects.filter(status_cook=False) # pylint: disable=no-member
    orderitems = OrderItem.objects.all() # pylint: disable=no-member

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        try:
            order = Order.objects.get(id=order_id) # pylint: disable=no-member
            order.status_cook = not order.status_cook
            order.save()
            messages.success(request, 'Статус приготовления заказа')
            return redirect('restaurant_ordering:cooking_list')
        except Order.DoesNotExist: # pylint: disable=no-member
            # Обработка исключения, если заказ не найден
            messages.error(request, 'Заказ с таким ID не найден.')
            return redirect('restaurant_ordering:cooking_list')

    return render(request, 'restaurant_ordering/cooking_list.html',
                  {'orders': orders,
                   'orderitems': orderitems})


@login_required
@is_delivery_decorator
def delivery_list(request):
    """ Получаем все заказы, где требуется доставка или оплата.
     Меняем статус доставки с False на True и наоборот.(Не доставлено/Доставлено)"""
    orders = Order.objects.filter(status_cook=True).exclude( # pylint: disable=no-member
        payment_state=True, status_delivery=True)

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        try:
            order = Order.objects.get(id=order_id) # pylint: disable=no-member
            order.status_delivery = not order.status_delivery
            order.save()
            messages.success(request, 'Статус доставки успешно изменен.')
        except Order.DoesNotExist: # pylint: disable=no-member
            # Обработка исключения, если заказ не найден
            messages.error(request, 'Заказ с таким ID не найден.')

    return render(request, 'restaurant_ordering/delivery_list.html',
                  {'orders': orders})


@login_required
@is_delivery_decorator
def payment_status_update(request):
    """Изменить статус оплаты с False на True и наоборот. (Не оплачено/Оплачено)"""

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        try:
            order = Order.objects.get(id=order_id) # pylint: disable=no-member
            order.payment_state = not order.payment_state
            order.save()
            messages.success(request, 'Статус оплаты успешно изменен.')
        except Order.DoesNotExist: # pylint: disable=no-member
            # Обработка исключения, если заказ не найден
            messages.error(request, 'Заказ с таким ID не найден.')

    return redirect('restaurant_ordering:delivery_list')
