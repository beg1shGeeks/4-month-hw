from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from book.views import helloview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('book.urls')),
    path('api/v1/', include('phone_app.urls')),
    path('hello/', helloview, name='hello')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)