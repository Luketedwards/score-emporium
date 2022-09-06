from django.contrib import admin
from .models import ScoreRequest, Comments, ScoreSubmissions

# Register your models here.

class ScoreRequestAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'date',
        'upvotes',
        'created_by',
        'video_link',
        'link',   
    )


admin.site.register(ScoreRequest, ScoreRequestAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'created_by',
        'date',
    )

class ScoreSubmissionsAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'created_by',
        'date',
    )

admin.site.register(Comments, CommentAdmin)
admin.site.register(ScoreSubmissions, ScoreSubmissionsAdmin)

