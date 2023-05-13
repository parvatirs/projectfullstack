from django.contrib import admin
from .models import Book


@admin.register(Book)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Book._meta.get_fields()]
