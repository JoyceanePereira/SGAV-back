from django.urls import URLPattern, path
from usuarios import views
urlpatterns= [
    path('', views.home),
    path('dashboard', views.dashboard),
    path('card', views.card),
    path('cardpessoal', views.cardpessoal),
    path('perfil', views.perfil),
]