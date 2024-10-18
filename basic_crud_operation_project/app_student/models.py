from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField(default=0)

    def __str__(self):
        return self.name  # Optional: useful for representing objects as strings in Django admin or shell

