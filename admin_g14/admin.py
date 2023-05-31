from django.contrib import admin

# Register your models here.
from admin_g14.models import *

# Register your models here.
myModels = [Organization,User,Location,WasteCat,WasteItem,WasteLog]
admin.site.register(myModels)