from django.contrib import admin
from .models import  User, UserProfile
from django.contrib.auth.admin import UserAdmin

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    
# class UserAdmin(admin.ModelAdmin):
class UserAdmin(UserAdmin):

    list_display = ('id', 'username', 'fullname', 'email')
    list_display_links = ('username', )
    list_filter = ('username', )
    search_fields = ('username', 'email', )

    fieldsets = (
        ("info", {'fields': ('username', 'password', 'email', 'fullname', 'join_date',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active', )}),)

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date', )
        else:
            return ('join_date', )

    inlines = (
        UserProfileInline,
    )

    add_fieldsets = (
        (
            None, {
                'classes' : ('wide', ),
                'fields' : ('email', 'fullname', 'password', ) 
            }
        )
    )

admin.site.register(UserProfile)
admin.site.register(User, UserAdmin)