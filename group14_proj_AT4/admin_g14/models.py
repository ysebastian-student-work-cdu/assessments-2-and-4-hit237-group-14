from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=150,unique=True)
    address = models.CharField(max_length=100)
    ADDRESS = [('ACT',"Australian Capital Territory"),('VIC','Victoria'),('NSW','New South Wales'),('WA','WA'),('NT','NT'),('QLD','QLD')]
    state = models.CharField(max_length=10,choices=ADDRESS)
    
    def __str__(self):
        return self.name

class Role(models.Model):
    titile = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    organization_name = models.ForeignKey(Organization,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.code

class User(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE,to_field='name')
    name = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    
class WasteCat(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
    
class WasteItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=120)
    waste_category = models.ForeignKey(WasteCat,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class WasteLog(models.Model):
    log_id = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=100)
    location = models.ManyToManyField(Location)
    organization = models.ManyToManyField(Organization)
    waste_item = models.ManyToManyField(WasteItem)
    waste_quantity = models.FloatField()
    datetime = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.audit_id
    

    