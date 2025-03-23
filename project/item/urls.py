from django.urls import path
from .views import ItemListCreate, ItemRetrievUpdateDestroy

urlpatterns = [
    path('/items', ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrievUpdateDestroy.as_view(), name = 'item-retrieve-update-destroy'),
]