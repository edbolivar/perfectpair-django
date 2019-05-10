from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from .views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', home, name='home'),
    path('shoe/', include('shoe.urls', namespace='shoe')), 
    path('customerservice/', include('customerservice.urls', namespace='customerservice')), 
    path('cart/', include('cart.urls', namespace='cart')), 
    path('authenticate/', include('authenticate.urls', namespace='authenticate')),


]







#if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



