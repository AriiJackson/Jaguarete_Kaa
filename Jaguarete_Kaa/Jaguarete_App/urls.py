from django.urls import path
from Jaguarete_App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('about/', views.about, name="About"),
    path('categoria/', views.categoria, name="Categoria"),
    path('carrito/', views.carro, name="Carrito"),
    path('login/', views.login, name="LogIn"),
    path('register/', views.register, name="Register"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)