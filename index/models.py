from django.db import models
from users.models import User


# Create your models here.
class LINK(models.Model):
    url = models.URLField(max_length=100, help_text="Enter a link of a website")
    name = models.CharField(max_length=100, help_text="Enter the name of a website")
    user = models.ManyToManyField(User)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.url
