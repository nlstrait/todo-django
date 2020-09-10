from django.contrib import admin
from .models import TodoItem, TodoList

admin.site.site_header = "Todo Admin"
admin.site.site_title = "Todo Admin Area"
admin.site.index_title = "Welcome to the Todo Admin Area"

#admin.site.register(TodoItem)
#admin.site.register(TodoList)

class TodoItemInLine(admin.TabularInline):
    model = TodoItem

class TodoListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        #('Date Information', {'fields': ['post_date'], 'classes': 'collapse'})
    ]
    inlines = [TodoItemInLine]

admin.site.register(TodoList, TodoListAdmin)