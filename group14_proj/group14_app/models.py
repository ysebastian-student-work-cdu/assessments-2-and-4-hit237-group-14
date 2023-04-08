from django.db import models

# Create your models here.


# List view
class FoodWaste(models.Model):
    TYPE_CHOICES = [
        ('household', 'Household waste'),
        ('retail', 'Retail waste'),
        ('restaurant', 'Restaurant waste'),
        ('agricultural', 'Agricultural waste'),
        ('processing', 'Processing waste'),
        ('transportation', 'Transportation and distribution waste'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.get_type_display()}: {self.description}"
