from django.shortcuts import render, redirect
from .models import Player, Item, Inventory

# Create your views here.
def index(request):
    context = {
        'all_players': Player.objects.all(),
        'all_items': Item.objects.all()
    }
    return render(request, "index.html", context)

def add_player(request):
    Player.objects.create(name=request.POST['name'],icon=request.POST['icon'])
    return redirect("/")

def add_item(request):
    Item.objects.create(name=request.POST['name'],effect=request.POST['effect'],icon=request.POST['icon'])
    return redirect("/")

def equip(request):
    context = {
        'all_players': Player.objects.all(),
        'all_items': Item.objects.all()
    }
    return render(request, "equip.html", context)

def add_inven(request):
    this_player = Player.objects.get(id=request.POST['player'])
    this_item = Item.objects.get(id=request.POST['item'])
    Inventory.objects.create(player=this_player,item=this_item)
    return redirect("/equip")

def delete_item(request, id):
    item_to_delete = Item.objects.get(id=id)
    item_to_delete.delete()
    return redirect("/")

def player_delete(request, id):
    player_to_delete = Player.objects.get(id=id)
    player_to_delete.delete()
    return redirect("/")

def remove_item(request, iid, pid):
    oneitem = Item.objects.get(id=iid)
    oneplayer = Player.objects.get(id=pid)
    items = Inventory.objects.filter(item = oneitem).filter(player = oneplayer).first()
    items.delete()
    return redirect("/equip")