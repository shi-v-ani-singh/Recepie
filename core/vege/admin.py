from django.contrib import admin

# Register your models here. 
# for admin view
from .models import *

admin.site.register(Recipe)