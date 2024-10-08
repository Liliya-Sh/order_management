"""
Модели для приложения restaurant_ordering.
"""

from django.contrib.auth import get_user_model
from django.db import models


class Menu(models.Model): # pylint: disable=too-few-public-methods
    """Модель, представляющая блюда/продукты ресторана."""

    class Status(models.IntegerChoices): # pylint: disable=too-few-public-methods
        """Статус наличия блюда/продукта в ресторане"""

        ABSENT = 0, 'Отсутствует'
        AVAILABILITY = 1, 'Вналичие'

    name_product = models.CharField(max_length=200,
                                    verbose_name='Наименование блюда')
    slug = models.SlugField(max_length=200,
                            db_index=True)
    description = models.TextField(max_length=500,
                                   null=True,
                                   verbose_name='Состав')
    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                verbose_name='Цена')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата добавления в меню')
    updated = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата изменения')

    objects = models.Manager()

    class Meta: # pylint: disable=too-few-public-methods
        """Метаданные для модели Menu."""

        ordering = ('name_product',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Customer(models.Model): # pylint: disable=too-few-public-methods
    """Модель, представляющая данные покупателя."""

    name = models.CharField(max_length=50,
                            null=True,
                            verbose_name='Имя покупателя')
    phone_number = models.CharField(max_length=35,
                                    verbose_name="Номер телефона покупателя")
    address = models.TextField(null=True,
                               blank=True,
                               verbose_name="Адрес доставки")

    class Meta:  # pylint: disable=too-few-public-methods
        """Метаданные для модели Customer."""

        ordering = ['pk']
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Order(models.Model): # pylint: disable=too-few-public-methods
    """Модель, представляющая заказ, сделанный покупателем."""

    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True,
                                 verbose_name='Клиент')
    creation_time = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Дата создания заказа')
    amount = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 verbose_name='Сумма заказа')
    comment = models.TextField(blank=True,
                               null=True,
                               verbose_name='Комментарий к заказу')
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.SET_NULL,
                             null=True, default=True)
    status_cook = models.BooleanField(default=False,
                                      verbose_name="Статус приготовления заказа")
    status_delivery = models.BooleanField(default=False,
                                          verbose_name="Статус доставки")
    payment_state = models.BooleanField(default=False,
                                        verbose_name="Статус оплаты")
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name='Дата изменения заказа')

    class Meta:  # pylint: disable=too-few-public-methods
        """Метаданные для модели Order."""

        ordering = ['pk']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        """Возвращает строковое представление объекта Order."""
        return f"Заказ {self.pk} от {self.customer}"


class OrderItem(models.Model): # pylint: disable=too-few-public-methods
    """Модель, представляющая составные части заказа."""
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              null=True,
                              verbose_name='id заказа')
    product = models.ForeignKey(Menu,
                                on_delete=models.CASCADE,
                                null=True,
                                verbose_name='Наименование продукта')
    quantity = models.PositiveIntegerField(default=1,
                                           verbose_name='Количество')
    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                verbose_name='Цена')
    discount = models.DecimalField(max_digits=6,
                                   decimal_places=2,
                                   default=0,
                                   verbose_name='Скидка в %')

    class Meta:  # pylint: disable=too-few-public-methods
        """Метаданные для модели OrderItem."""

        ordering = ['pk']
        verbose_name = 'Продукт в заказе'
        verbose_name_plural = 'Продукт в заказе'

    def get_cost(self):
        """Возвращает стоимость заказа с учетом количества."""

        return round(self.price * self.quantity, 2)
