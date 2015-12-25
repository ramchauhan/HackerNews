from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import NewsItem, UserProfile
from .forms import UserChangeForm, UserCreationForm


class NewsItemAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "hacker_news_url", "url", "posted_on", "upvotes", "comments",
                    "created_date", "modified_date"]


class UserProfileAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'user_name', 'is_superuser')
    list_filter  = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('user_name',)}),
        ('Permissions', {'fields': ('is_superuser', 'user_permissions', )}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields'  : ('email', 'user_name', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'user_name')
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(UserProfile, UserProfileAdmin)
# ... and, since we're not using Django's builtin permissions,
# un register the Group model from admin.
admin.site.unregister(Group)
admin.site.register(NewsItem, NewsItemAdmin)

