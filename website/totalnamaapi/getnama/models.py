from django.db import models

# Create your models here.
class HitungNama(models.Model):
    nama = models.CharField(max_length=100)
    total = models.IntegerField()
    totalnamalaki = models.IntegerField()
    totalnamaperempuan = models.IntegerField()