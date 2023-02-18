from django.urls import path
from . import views
from .views import change_password


urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('index', views.index, name='index'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('change_password', views.change_password, name='change_password'),
    path('commande', views.commande, name='commande'),
    path('livraison', views.livraison, name='livraison'),
    path('suivi', views.suivi, name='suivi'),
    path('produit', views.produit, name='produit'),
    path('add_product', views.add_product, name='add_product'),
    path('produit/edit_product/<int:id>', views.edit_product, name='edit_product'),
    path('produit/delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('niveau', views.niveau, name='niveau'),
    path('create_n1', views.create_n1, name='create_n1'),
    path('create_n2', views.create_n2, name='create_n2'),
    path('create_n3', views.create_n3, name='create_n3'),
    path('create_n4', views.create_n4, name='create_n4'),
    path('create_n5', views.create_n5, name='create_n5'),
]