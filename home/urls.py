from django.urls import include, path
from home import views
from rest_framework import routers
from .views import  resumeHomeAPIVIEW


urlpatterns = [
    
    path('resume-home/',resumeHomeAPIVIEW.as_view() ) 
]
