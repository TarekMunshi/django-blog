from django.db import models


class BlogPost(models.Model):
    title = models.TextField()
    authorName = models.CharField(max_length=255)
