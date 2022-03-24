from datetime import date
from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    content = models.TextField()
    issue_date = models.DateField(blank=True, default=date.today)

    def __str__(self) -> str:
        return "message from " + self.name  