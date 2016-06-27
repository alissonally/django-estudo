from django.contrib import admin

from .models import Post, Author, Category, Tag

class AutoSlug(admin.ModelAdmin):
	prepopulated_fields = {'post_slug':('post_title',)}

admin.site.register(Post, AutoSlug)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)
