from django.db import models

# Create your models here.
class job(models.Model):
    image = models.ImageField(upload_to='images1/')
    summary = models.CharField(max_length=30)

    def __str__(self):
        return self.summary
