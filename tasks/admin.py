from django.contrib import admin
from .models import Task



class TaskAdmin(admin.ModelAdmin):
    list_display = ('content', 'user')
    fields = ['content', 'user']


admin.site.register(Task, TaskAdmin)