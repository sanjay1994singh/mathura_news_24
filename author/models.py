from django.db import models

from accounts.models import User


# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'author'
