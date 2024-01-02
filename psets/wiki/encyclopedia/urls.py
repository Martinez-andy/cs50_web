from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wikiPage, name="wiki"),
    path("search/", views.search, name="search"),
    path("randompage/", views.randomPage, name="randomPage"),
    path("newpage/", views.newPage, name="newPage"), 
    path("edit/", views.editPage, name="editPage"),
    path("saveEdit/", views.saveEdit, name="saveEdit"),
]
