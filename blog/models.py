from django.db import models

# Create your models here.

#Create a blog model
#add the blog app to the setting
#create migrations
#migrate
#add to admin


class blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title
