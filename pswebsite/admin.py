from django.contrib import admin

from pswebsite import models

class PosterImageInline(admin.TabularInline):
    model = models.PosterImage
    extra = 2

class PosterAdmin(admin.ModelAdmin):
    inlines = [PosterImageInline]

    def save_model(self, request, obj, form, change):
        """When creating a new object, set the user_creator field.
        """
        if not change:
            obj.user_creator = request.user
            obj.save()

# TODO: reorder the fields for dimension so it is correct width x height

admin.site.register(models.Poster, PosterAdmin)
admin.site.register(models.PosterDimension)
admin.site.register(models.PosterImage)
