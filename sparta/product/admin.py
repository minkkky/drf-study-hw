from django.contrib import admin
from .models import Product, Review


class ReviewInline(admin.StackedInline):
    model = Review

# class UserAdmin(admin.ModelAdmin):
class ProductAdmin(admin.ModelAdmin):

        list_display = ('id', 'thumbnail_preview', 'title', 'price', 'start_date', 'end_date',  'author', )
        list_display_links = ('title',  'thumbnail_preview',)
        list_filter = ('author', 'price',  'start_date', 'end_date', )
        search_fields = ('author', 'title', 'price', )

        fieldsets = (
        ('Product', {'fields': ('title', 'thumbnail_preview','thumbnail', 'desc', 'price', 'author', )}),
        ('Permissions', {'fields': ('start_date', 'end_date', 'is_active', )}),
        )

        readonly_fields = ('thumbnail_preview',)

        def thumbnail_preview(self, obj):
                return obj.thumbnail_preview

        thumbnail_preview.short_description = 'Thumbnail Preview'
        thumbnail_preview.allow_tags = True

        filter_horizontal = []

        # def get_readonly_fields(self, request, obj=None):
        #         if obj:
        #                 return ('username', 'join_date', )
        #         else:
        #                 return ('join_date', )

        inlines = (
        ReviewInline,
        )

        # add_fieldsets = (
        # (
        # None, {
        # 'classes' : ('wide', ),
        # 'fields' : ('email', 'fullname', 'password', ) 
        # }
        # )
        # )

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)