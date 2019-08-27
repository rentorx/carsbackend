from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Account


# Define an inline admin descriptor for Account model
# which acts a bit like a singleton
class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'accounts'
    fk_name = 'user'


# Define a new User admin
class CustomUserAdmin(UserAdmin):
    inlines = (AccountInline,)
    list_display = ['id', 'username', 'last_login', 'date_joined', ]
    search_fields = ['email', 'username']


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
