from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="inicio"),
    path('register/', views.register_view, name='register_view'),
]
