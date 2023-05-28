from django.contrib import admin

# Register your models here.
from admin_g14.models import *

# Register your models here.
myModels = [Organization,Role,User,Location,WasteCat,WasteItem,Audit]
admin.site.register(myModels)