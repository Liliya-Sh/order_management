"""
Миграция для приложения restaurant_ordering.
"""

# Generated by Django 4.2.1 on 2024-09-13 15:55
# pylint: skip-file

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Миграция для добавления поля 'user' в модель 'Order'."""

    initial = True

    dependencies = [
        ('restaurant_ordering', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=True,
                                    null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterIndexTogether(
            name='menu',
            index_together={('id', 'slug')},
        ),
    ]
