from django.urls import path

from todoapp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('viewtitle',views.viewtitle,name='viewtitle'),
    path('addtodo',views.addtodo,name='addtodo'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]