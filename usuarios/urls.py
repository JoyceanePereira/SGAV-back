from django.urls import URLPattern, path
from usuarios import views
urlpatterns= [
    path('', views.home),
    path('dashboard', views.dashboard)
]