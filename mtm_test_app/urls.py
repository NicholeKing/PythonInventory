from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('add_player', views.add_player),
    path('add_item', views.add_item),
    path('equip', views.equip),
    path('add_inven', views.add_inven),
    path('player_delete/<int:id>', views.player_delete),
    path('delete_item/<int:id>', views.delete_item),
    path('remove_item/<int:iid>/<int:pid>', views.remove_item)
]