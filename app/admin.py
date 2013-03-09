from django.contrib import admin
from app.models import Event, Demo, Comment

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'datetime', 'is_current')

class DemoAdmin(admin.ModelAdmin):
    list_display = ('presenter', 'email', 'title')

class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Demo, DemoAdmin)
admin.site.register(Comment, CommentAdmin)