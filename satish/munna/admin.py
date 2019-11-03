from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *
from .models import tudent

from .models import Satish,Hello,Customer,Navbar

class CustomerAdmin(ModelAdmin):
    list_display=["Customer_Name"]
    search_fields=["Customer_Name","Salary"]


admin.site.register(tudent)
admin.site.register(Navbar)
admin.site.register(Satish)
admin.site.register(Hello)
admin.site.register(Customer,CustomerAdmin)
