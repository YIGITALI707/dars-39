from django.urls import path
from . import views

urlpatterns = [
    path('brands/', views.BrandListCreateView.as_view()),
    path('brands/<int:pk>/', views.BrandDetail.as_view()),
    path('cars/', views.CarListCreateView.as_view()),
    path('cars/<int:pk>/', views.CarDetail.as_view()),
    path('colors/', views.ColorListCreateView.as_view()),
    path('colors/<int:pk>/', views.ColorDetail.as_view()),
]

