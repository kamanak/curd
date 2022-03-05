from django.contrib import admin
from django.urls import path,include
from curdapp import views

urlpatterns = [
    path("",views.add,name = "add"),
    path('delete/<int:id>/',views.delete,name="deletedata"),
    path('<int:id>/',views.update,name="updatedata"),

   
   
    
]