from django.urls import path
from .import views

urlpatterns = [
    
     path('', views.index, name= "index"),
     path ('chandan', views.chandan, name = "chandan"),
     path ('views.aboutus/', views.aboutus, name = "aboutus"),
     path ('views.contactus/', views.contactus, name = "contactus"),
     #path ('chandan/views.aboutus/', views.aboutus, name = "aboutus"),

]