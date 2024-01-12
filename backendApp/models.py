from django.db import models

class FavStocks(models.Model):
    name = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)
    price = models.FloatField()
    added = models.BooleanField(False)
    change = models.FloatField()
    #changePer = models.FloatField()
    movement = models.CharField(max_length=255)

    def __str__(self):
        return self.companyName
