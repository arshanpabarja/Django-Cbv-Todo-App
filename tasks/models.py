from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, models.CASCADE,null=True, blank=True)
    content = models.CharField(max_length=60, blank=False, null=False)
    done = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.content