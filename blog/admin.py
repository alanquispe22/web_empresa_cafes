from django.contrib import admin
from .models import Category, Post
from django.utils.safestring import mark_safe

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','author','published','post_categories')
    ordering = ('author','published')
    search_fields = ('title','content','author__username')
    date_hierarchy = 'published' # Navegación entre fechas
    list_filter = ('author__username','categories__name') # Mas para claves foraneas

    def post_categories(self,obj):
        return mark_safe('<b>%s</b>'%", ".join([c.name for c in obj.categories.all().order_by("name")]))
    
    post_categories.short_description = "Caterorías"


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)