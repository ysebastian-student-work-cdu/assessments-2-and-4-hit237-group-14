from django.db import models

# Create your models here.

#below is the codes to define the "Profile" and "Introduction" model in our
#group14_app's models.py
#created by putu (from line 8-32)
GENDER = [
    ("M", "Male"),
    ("F", "Female"),
]
class Profile(models.Model):
    Full_Name = models.CharField(max_length=50)
    Student_Id = models.CharField(max_length=10)
    Gender = models.CharField(max_length=1, choices=GENDER)
    
    def __str__(self):
        return self.Full_Name
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Team Members Profile"
        
class Introduction(models.Model):
    Brief = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.Brief
    
    class Meta:
        verbose_name = "Explanation"
        verbose_name_plural = "Website Introduction"

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

class FoodDetail(models.Model):
    name = models.CharField(max_length=200, null=True, help_text="Waste Name")
    desc = models.TextField()
