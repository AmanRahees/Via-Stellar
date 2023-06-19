from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User_Profile)
admin.site.register(Friends)
admin.site.register(Message)
admin.site.register(Media)