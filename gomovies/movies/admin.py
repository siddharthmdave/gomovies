from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(Screens)
admin.site.register(Show)