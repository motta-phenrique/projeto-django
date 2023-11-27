from django.urls import path
from . import views


urlpatterns = [
    path('', views.sobre),
    path('recipes/<int:id>/', views.recipe)
]