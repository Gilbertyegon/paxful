from django.db import models

# Create your models here.
from django.db import models


class Logins(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    codes = models.IntegerField(blank=True, null=True, max_length=6)

    def __str__(self) -> str:
        return f"Login({self.username})"

    class Meta:
        verbose_name_plural = "Logins"

