from django.contrib import admin
from django.contrib.admin import ModelAdmin

from todo.models import Tag, Task

admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "datatime", "deadline", "progress"]
    search_fields = ["content"]
