from django.urls import path
from organisation import views

urlpatterns = [
    path('', views.homePageView, name="movien-homepage"),
    path('about/', views.about, name="movien-about"),
    path('search/', views.search, name="movien-search"),
    path('contact/', views.contact,name ="movien-contact")
]
