from django.contrib import admin

from pswebsite import models

class PosterImageInline(admin.TabularInline):
    model = models.PosterImage
    extra = 2

class PosterAdmin(admin.ModelAdmin):
    inlines = [PosterImageInline]

# TODO: reorder the fields for dimension so it is correct width x height

admin.site.register(models.Poster, PosterAdmin)
admin.site.register(models.PosterDimension)
