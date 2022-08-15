from django.contrib import admin
from .models import ScoreRequest

# Register your models here.

class ScoreRequestAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'date',
        'created_by',
        'upvotes',
        
        'video_link',
        'link'
        
    )

admin.site.register(ScoreRequest, ScoreRequestAdmin)