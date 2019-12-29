from django.contrib import admin
from .models import Actor, Task, Comment

# Register your models here.
admin.site.register(Task)
admin.site.register(Actor)
admin.site.register(Comment)