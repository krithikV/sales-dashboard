from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_sale = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.product} - {self.date}"