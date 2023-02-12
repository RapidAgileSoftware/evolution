from django.db import models


class Pond(models.Model):
    name: models.CharField()
    sizeX: models.IntegerField()
    sizeY: models.IntegerField()
    sizeZ: models.IntegerField()


class Location(models.Model):
    pond = models.ForeignKey(
        Pond,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True

    positionX = models.PositiveIntegerField()
    positionY = models.PositiveIntegerField()
    positionZ = models.PositiveIntegerField()

    previousPositionX = models.PositiveIntegerField()
    previousPositionY = models.PositiveIntegerField()
    previousPositionZ = models.PositiveIntegerField()

    sizeX = models.PositiveSmallIntegerField()
    sizeY = models.PositiveSmallIntegerField()
    sizeZ = models.PositiveSmallIntegerField()

    currentSpeed = models.SmallIntegerField()


class Resource(Location):

    isAlive = models.BooleanField()
    mass = models.PositiveIntegerField()


class Life(models.Model):
    resource = models.OneToOneField(
        Resource,
        on_delete=models.CASCADE,
     )

    dna = models.TextField()
    devourPower = models.PositiveSmallIntegerField()
    energyStore = models.PositiveSmallIntegerField()
    scanRadius = models.PositiveSmallIntegerField()
    health = models.PositiveSmallIntegerField()

    parentOne = models.ForeignKey('self', on_delete=models.CASCADE)
    parentTwo = models.ForeignKey('self', on_delete=models.CASCADE)
