from django.db import models

# Create your models here.
class Pendaftar(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=75)
    no_hp = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    def __str__(self):
        # return self.nama
        return f"{self.nama} - {self.alamat} - {self.no_hp} - {self.email}"



