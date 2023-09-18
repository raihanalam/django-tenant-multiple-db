from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    deadline = models.DateField()

    def __str__(self):
        return self.name
