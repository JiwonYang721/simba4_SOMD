from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('',mainpage, name="mainpage"),
    path('board/',board,name="board"),
    path('register/',register,name="register"),
    path('mysomd/',mysomd,name="mysomd"),
    path('createSOMD/',createSOMD,name="createSOMD"),
    path('mainfeed/<int:id>',mainfeed,name="mainfeed"),
    path('join/', join,name="join"),
    path('members/',members,name="members"),
]