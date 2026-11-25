from django.contrib import admin
from .models import Swiggy, SwiggyAdmin

# Register your models here.
admin.site.register(Swiggy,SwiggyAdmin)