from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #how it appears in the model view in admin (not inserting)
    list_display = ['title' , 'slug' , 'author' , 'publish' , 'status']
    #Add sidebar to filter by these
    list_filter = ['status', 'created', 'publish', 'author']
    #add a search box wordu by wordu ~! in title and body ~!
    search_fields = ['title', 'body']
    #Automatically fills the slug field based on the title as you type it.
    prepopulated_fields = {
        'slug': ('title',)
        }
    #instead of drop-down menu for foreign , we will have lookup!
    raw_id_fields = ['author']
    #Adds a date-based drill-down navigation at the top of the changelist
    date_hierarchy = 'publish'
    # order by status , publish :c
    ordering = ['status', 'publish']
    