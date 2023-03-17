from django.contrib import admin

# Register your models here.
from .models import Room,Route,Message

admin.site.register(Room)
admin.site.register(Route)
admin.site.register(Message)