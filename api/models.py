from django.db import models

# Create your models here.
# admin200


class Fundings(models.Model):
    title = models.CharField(max_length=1000)
    status = models.BooleanField(max_length=100)
    deadline = models.CharField(max_length=5000, blank=True)
    eligibility = models.CharField(max_length=5000, blank=True)
    url = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=10000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ministry = models.ForeignKey(
        'Ministry', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Ministry(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
