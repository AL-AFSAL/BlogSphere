from django.urls import path ,include
from . import views

app_name = "blog"  # Correct way to set the namespace

urlpatterns = [

    path("", views.index, name="index"),
    #you can give any kind of datatypes for dynamic segemants
    path("post/<str:slug>", views.post, name="post"),
    path("new_url_is-one", views.new_url_view, name="new_url_view"),
    path("old_url", views.old_url_redirect, name="old_url"),
    path("contact", views.contact_views, name="contact"),
    path("aboutus", views.aboutus_views, name="aboutus"),


]