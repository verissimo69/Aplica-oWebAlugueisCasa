from django.contrib import admin
from todos import models

# Register your models here.
admin.site.register(models.Client)

class ImmobileImageInlineAdmin(admin.TabularInline):
    model = models.ImmobileImage
    extra = 0

class ImmobileAdmin(admin.ModelAdmin):
    inlines = [ImmobileImageInlineAdmin]

admin.site.register(models.Immobile, ImmobileAdmin)
admin.site.register(models.RegisterLocation)