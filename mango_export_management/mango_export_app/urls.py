from django.urls import path
from .views import mango_list, mango_create, mango_update, mango_delete

# urlpatterns = [
#     path('', mango_list, name='mango_list'),
#     path('new/', mango_create, name='mango_create'),
#     path('edit/<int:id>/', mango_update, name='mango_update'),
#     path('delete/<int:id>/', mango_delete, name='mango_delete'),
# ]
urlpatterns = [
    path('', mango_list, name='mango_list'),
    path('new/', mango_create, name='mango_create'),
    path('edit/<int:order_id>/', mango_update, name='mango_update'),  # Updated: order_id
    path('delete/<int:order_id>/', mango_delete, name='mango_delete'),  # Updated: order_id
]