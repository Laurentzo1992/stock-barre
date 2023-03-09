from django.urls import path
from . import views
from .views import ExportProductsCSVView, ExportProductsExcelView
from stock.views import SearchProductView

urlpatterns = [
    path('index', views.index, name='index'),
    path('client', views.client, name='client'),
    path('add_client', views.add_client, name='add_client'),
    path('edit_client/<int:id>', views.edit_client, name='edit_client'),
    path('delete_client/<int:id>', views.delete_client, name='delete_client'),
    path('transport', views.transport, name='transport'),
     path('add_transport', views.add_transport, name='add_transport'),
    path('edit_transport/<int:id>', views.edit_transport, name='edit_transport'),
    path('delete_transport/<int:id>', views.delete_transport, name='delete_transport'),
    path('commande', views.commande, name='commande'),
    path('print_commande/<int:pk>', views.print_commande, name='print_commande'),
    path('print_commande2/<int:pk>', views.print_commande2, name='print_commande2'),
    path('livraison', views.livraison, name='livraison'),
    path('edit_livraison/<int:livraison_id>', views.edit_livraison, name='edit_livraison'),
    path('edit_livraison2/<int:livraison_id>', views.edit_livraison2, name='edit_livraison2'),
    path('suivi', views.suivi, name='suivi'),
    path('produit', views.produit, name='produit'),
    path('search_product/', SearchProductView.as_view(), name='search_product'),
    path('add_product', views.add_product, name='add_product'),
    path('produit/edit_product/<int:id>', views.edit_product, name='edit_product'),
    path('produit/delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('export/csv/', ExportProductsCSVView.as_view(), name='export_products_csv'),
    path('export/excel/', ExportProductsExcelView.as_view(), name='export_products_excel'),
    path('stock_in', views.stock_in, name='stock_in'),
    path('operation_print/<int:id>', views.operation_print, name='operation_print'),
    path('stock_barre', views.stock_barre, name='stock_barre'),
    path('add_stock', views.add_stock, name='add_stock'),
    path('niveau', views.niveau, name='niveau'),
    path('create_n1', views.create_n1, name='create_n1'),
    path('niveau/edit_n1/<int:id>', views.edit_n1, name='edit_n1'),
    path('create_n2', views.create_n2, name='create_n2'),
    path('niveau/edit_n2/<int:id>', views.edit_n2, name='edit_n2'),
    path('create_n3', views.create_n3, name='create_n3'),
    path('niveau/edit_n3/<int:id>', views.edit_n3, name='edit_n3'),
    path('create_n4', views.create_n4, name='create_n4'),
    path('niveau/edit_n4/<int:id>', views.edit_n4, name='edit_n4'),
    path('create_n5', views.create_n5, name='create_n5'),
    path('niveau/edit_n5/<int:id>', views.edit_n5, name='edit_n5'),
]