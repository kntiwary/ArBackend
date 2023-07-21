from django.db import models

# Create your models here.
from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Floor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='floors')
    floor_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.building.name} - Floor {self.floor_number}"


class Room(models.Model):
    name = models.CharField(max_length=100)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.floor.building.name} - Floor {self.floor.floor_number} - Room {self.room_number}"


class Marker(models.Model):
    name = models.CharField(max_length=100)
    anchor_id = models.CharField(max_length=50, unique=True)
    tx = models.FloatField()
    ty = models.FloatField()
    tz = models.FloatField()
    qx = models.FloatField()
    qy = models.FloatField()
    qz = models.FloatField()
    qw = models.FloatField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, blank=True, null=True, related_name='markers')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True, related_name='markers')

    def __str__(self):
        return f"Anchor ID: {self.anchor_id}, Name: {self.name}"
