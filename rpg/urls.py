from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from IA import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.generate_image, name='index')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
