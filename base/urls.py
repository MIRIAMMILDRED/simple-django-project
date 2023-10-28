from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('root/<int:pk>', views.root, name="root")
    
]


