from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})