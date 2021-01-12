from django.contrib import admin

# Register your models here.
from .models import Blog, Category

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, PostAdmin)
admin.site.register(Category, CategoryAdmin)