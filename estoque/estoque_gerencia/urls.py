from django.urls import path, include
from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.home, name='home'),
    path('list_item/', views.list_item, name='list_item'),
    path('add_item/', views.add_item, name='add_item'),
    path('update_item/<pk>/', views.update_item, name='update_item'),
    path('delete_item/<pk>', views.delete_item, name='delete_item'),
    path('estoque_detail/<pk>/', views.estoque_detail, name='estoque_detail'),
    path('emitir_item/<pk>/', views.emitir_item, name="emitir_item"),
    path('receber_item/<pk>/', views.receber_item, name="receber_item"),
    path('nivel_reabastecimento/<pk>/', views.nivel_reabastecimento,
         name='nivel_reabastecimento'),
]
