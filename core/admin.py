from django.contrib import admin
from .models import Invitation, Birthday, Gallery

@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    list_filter = ('date',)
    search_fields = ('title', 'description')
    ordering = ('-date',)
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Event Details', {
            'fields': ('title', 'date', 'description')
        }),
        ('Meta Info', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth')
    list_filter = ('date_of_birth',)
    search_fields = ('name',)
    ordering = ('name',)
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'date_of_birth', 'message')
        }),
    )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'image_preview')
    search_fields = ('title',)
    readonly_fields = ('uploaded_at', 'image_preview')
    ordering = ('-uploaded_at',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" style="object-fit:cover;border-radius:8px;">'
        return "(No image)"
    image_preview.allow_tags = True
    image_preview.short_description = "Preview"
