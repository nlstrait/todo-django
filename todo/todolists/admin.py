from django.contrib import admin
from .models import TodoItem

admin.site.site_header = "Todo Admin"
admin.site.site_title = "Todo Admin Area"
admin.site.index_title = "Welcome to the Todo Admin Area"

admin.site.register(TodoItem)