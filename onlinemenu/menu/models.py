from django.db import models
from django.core.validators import MinValueValidator
import uuid
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=3, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Tabel(models.Model):
    STATUS_CHOICES = [
        ("empty", "خالی"),
        ("reserved", "رزرو شده"),
        ("full", "اشغال"),
    ]
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField(default=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="empty")
    qr_code_link = models.URLField(blank=True)

    def __str__(self):
        return f"میز {self.number}({self.get_status_display()})"

