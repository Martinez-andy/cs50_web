from django.urls import path


from . import views # Imports all the functions one can get from views

urlpatterns = [
    path("", views.index, name='index'), # The empty string sets this file as the default
    path('andy', views.andy, name='andy'),
    path('dalia', views.dalia, name='dalia'),
    path('<str:name>', views.greet, name='greet') # <str:name> takes any string as input and puts that into into out views.greet function
]
