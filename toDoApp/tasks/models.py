from django.db import models


# Create your models here.
class Task(models.Model):
    CHOICES = (
        ("Done", "Done"),
        ("InProgress", "In Progress"),
        ("NotStarted", "Not Started"),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)
    status = models.CharField(max_length=20, choices=CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.description}"
