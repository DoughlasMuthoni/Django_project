
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home"),
    path('about/', views.about_page, name="about"),
    path('contact/', views.contact_page, name= "contact"),
    path('course/', views.course_details_page, name="details"),
    path('courses/', views.courses_page, name="courses"),
    path('events/', views.events_page, name="events"),
    path('starter/', views.starter_page, name="starter"),
    path('trainers/', views.trainers_page, name="trainers"),
    path('pricing/', views.pricing_page, name="pricing"),
]