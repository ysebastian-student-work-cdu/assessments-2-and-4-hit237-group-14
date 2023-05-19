from django.db import models

class Contact(models.Model):
    name = models.CharField('Your Name', max_length=20)
    email = models.EmailField('Email Address', blank=True)
    subject = models.CharField('Subject', max_length=200)
    message = models.TextField('Message', max_length=500)
        
    def __str__(self):
        return self.name

class WasteType(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
class Measurement(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class WasteLog(models.Model):
    organisation = models.CharField(max_length=30)
    fullname = models.CharField(max_length=500)
    wastetype = models.ForeignKey(WasteType, on_delete=models.CASCADE)
    foodname = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    reason = models.CharField(max_length=100)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    foodsize = models.CharField(max_length=10)
    recorded = models.CharField(max_length=100)