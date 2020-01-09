from django.contrib.auth.models import User
from adventure.models import Player,Room


Room.objects.all().delete()

r_outside = Room(x=1,y=1,title="Outside Cave Entrance",
               description="North of you, the cave mount beckons")

r_foyer = Room(x=1,y=2,title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")


r_outside.save()
r_foyer.save()

r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

