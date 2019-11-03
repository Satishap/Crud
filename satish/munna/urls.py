from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index.html"),
    path('Hyy',views.Hyy,name="Hyy"),
    path('hello',views.hello,name="hello"),
    path('service',views.service, name="service"),
    path('Navbar', views.Navbar, name="Navbar"),
    path("blog", views.detail, name="detail"),
    path('website',views.website, name="Website"),
    
    
   
    
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
