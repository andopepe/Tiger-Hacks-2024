from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Index"),
    # path("cached", views.cached, name='cached'),
    # path("cacheless", views.cacheless, name='cacheless'),
    path("upload/", views.Upload, name="Upload"),

]