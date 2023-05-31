from django.contrib import admin

# Import models from models.py
from .models import Study

# Register your models here.

admin.site.register(Study)
