from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('user', views.index1,name='index1'),	 
    path('mm/<int:U_id>', views.addMessage,name='addMessage'),	  
    path('uu', views.addUser),
    path('create', views.creat),  
    path('dd/<int:M_id>', views.delete),
    path('cc/<int:U_id>/<int:M_id>', views.addComment,name='addComment'),
    path('login', views.Login,name='Login'), 	 
    path('logout', views.Logout,name='Logout'), 
]