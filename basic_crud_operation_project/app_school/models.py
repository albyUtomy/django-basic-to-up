
from django.db import models
from django.utils import timezone


class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
