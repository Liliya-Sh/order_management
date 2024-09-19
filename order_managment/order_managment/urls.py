from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found
from order_managment import settings

urlpatterns = [
    path('admin/', admin.site.urls), #http://127.0.0.1:8000/admin/
    path('worksite/', include('restaurant_ordering.urls')), #http://127.0.0.1:8000/worksite/
    path('', include('users_employee.urls', namespace='users_employee')), #http://127.0.0.1:8000/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found