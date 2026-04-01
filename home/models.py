from django.db import models

class Bien(models.Model):
    titre = models.CharField(max_length=200)
    prix = models.CharField(max_length=50)
    details = models.TextField()
    image = models.ImageField(upload_to='biens/')
    type_bien = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.titre