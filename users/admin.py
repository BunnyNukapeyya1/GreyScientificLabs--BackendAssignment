from django.contrib import admin
from .models import User,Patient,MedicalRecord
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Patient)
admin.site.register(MedicalRecord)
@admin.register(User)
# Register your models here.
class UserAdmin(UserAdmin):
    pass


