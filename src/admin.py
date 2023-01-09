from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(event)
admin.site.register(project)
admin.site.register(team_member)
admin.site.register(User)
admin.site.register(feed)