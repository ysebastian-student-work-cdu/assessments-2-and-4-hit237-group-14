from django.contrib import admin
from .models import Contact, WasteType, WasteLog, Measurement

# Register your models here.

admin.site.register(Contact)
admin.site.register(WasteLog)
admin.site.register(WasteType)
admin.site.register(Measurement)


