from django.db import models

# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField()

