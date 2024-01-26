from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('order-online/', views.order_view, name='order_online'),  
    path('contact/', views.contact_view, name='contact'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('search/', views.search_results, name='search_results'),  
    path('signup/', views.signup_view, name='signup'),  # Fix path and view function name
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
