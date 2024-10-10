from django.urls import path
from . import views

urlpatterns =[
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("projectstable/",views.projectstable,name="projectstable"),
    path("contact/",views.contact,name="contact"),
    path("resume/",views.resume,name="resume"),
    path("imageframe/",views.image,name="imageframe"),
    # path("blog2/",views.blog2,name="blog2"),


]