from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('product/add/', views.product_create, name='product_create'),
    path('notas/', views.nota_list, name='nota_list'),
    path('notas/add/', views.nota_create, name='nota_create'),
    path('notas/cbv/', views.NotaView.as_view(), name='nota_cbv'),
]
