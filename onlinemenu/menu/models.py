from django.db import models
from django.core.validators import MinValueValidator
import uuid
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=3, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = self.image.open(self.image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.image.path, quality=70, optimize=True)

    def __str__(self):
        return self.name

class Tabel(models.Model):
    number = models.CharField(max_length=10, unique=True, verbose_name="شماره میز ")
    unique_id = models.UUIDField(default=uuid.uuid4, editable= False, unique=True)
    is_active = models.BooleanField(default=True, verbose_name="میز فعال است؟")

    def __str__(self):
        return f"میز {self.number}"
    
