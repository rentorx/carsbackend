from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, User


# Define an inline admin descriptor for Account model
# which acts a bit like a singleton
class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'accounts'


# Define a new User admin
class CustomUserAdmin(UserAdmin):
    inlines = (AccountInline,)
    list_display = ['username', 'last_login', 'date_joined', 'is_company']
    search_fields = ['email', 'username']


# Re-register UserAdmin
#admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
