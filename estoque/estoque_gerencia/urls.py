from django.urls import path, include
from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.home, name='home'),
    path('list_item/', views.list_item, name='list_item'),
    path('add_item/', views.add_item, name='add_item'),
    path('update_item/<pk>/', views.update_item, name='update_item'),
    path('delete_item/<pk>', views.delete_item, name='delete_item'),
    path('estoque_detail/<pk>/', views.estoque_detail, name='estoque_detail')
]
