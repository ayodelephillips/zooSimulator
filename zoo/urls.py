from django.urls import path

from . import views
#feedzoo is a url that implements feedZoo action
#invokeHour is a url that allows the system provoke an hour and carry out the actions
#path with the name index points to the home page
urlpatterns=[
    path('',views.index,name='index'),
    path('feedZoo',views.feedZoo, name='feedZoo'),
    path('invokeHour',views.invokeHour, name='invokeHour')
]

