from django.db import models

class Contact(models.Model):
    name = models.CharField('Your Name', max_length=20)
    email = models.EmailField('Email Address', blank=True)
    subject = models.CharField('Subject', max_length=200)
    message = models.TextField('Message', max_length=500)
        
    def __str__(self):
        return self.name