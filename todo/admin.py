from django.contrib import admin
from .models import TaskList,TodoItem
class TodoItemInline(admin.TabularInline):
    model = TodoItem
    readonly_fields = ('slug',)

class TaskListAdmin(admin.ModelAdmin):
    list_select_related = ('list', 'category')
    inlines = (TodoItemInline,)
    readonly_fields = ('slug',)

admin.site.register(TaskList,TaskListAdmin)