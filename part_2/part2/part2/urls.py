from app import views as app_views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', app_views.home, name='home')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

