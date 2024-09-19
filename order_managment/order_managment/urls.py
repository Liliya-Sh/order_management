"""
URL конфигурация для приложения order_managment.
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found

from order_managment import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('worksite/', include('restaurant_ordering.urls')),
    path('', include('users_employee.urls', namespace='users_employee')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
