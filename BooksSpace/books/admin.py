from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(author)
admin.site.register(publishing)
admin.site.register(book)
admin.site.register(in_planes)