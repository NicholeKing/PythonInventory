from django.db import models

# Item
class Item(models.Model):
    name = models.CharField(max_length=45)
    effect = models.CharField(max_length=255)
    icon = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Player
class Player(models.Model):
    name = models.CharField(max_length=45)
    icon = models.TextField()
    player_inventory = models.ManyToManyField(Item, through="Inventory")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Inventory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
