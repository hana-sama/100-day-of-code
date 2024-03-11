from django.contrib import admin
from .models import Form
# Register your models here.

class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "date", "occupation")
    search_fields = ("first_name", "last_name", "email", "date", "occupation")
    list_filter = ("date", "occupation")
    ordering = ("first_name",)
    

admin.site.register(Form, FormAdmin)
