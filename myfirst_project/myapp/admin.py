from django.contrib import admin
from myapp.models import FireRecords

# Register your models here.
class FireRecordsAdmin(admin.ModelAdmin):
    pass

admin.site.register(FireRecords, FireRecordsAdmin)