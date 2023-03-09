from  django.urls import  path
from  . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('change_password', views.change_password, name='change_password'),
    path('auth/add', views.add_user, name="add_user"),
    path('auth/edit/<int:id>', views.edit_user, name="edit_user"),
    path('auth/delete/<int:id>', views.delete_user, name="delete_user"),
]
