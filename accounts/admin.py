from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CostumUserCreationForm
from accounts.models import CostumUser



class CostumUserAdmin(UserAdmin):
    model=CostumUser
    add_form = CostumUserCreationForm
    form = CostumUserCreationForm
    list_display = ['username', 'last_name', 'first_name', 'email', 'age', 'is_staff','male']
    add_fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age',)}),
                                           )
    fieldsets = UserAdmin.fieldsets + ((None,{'fields': ['age',]}),
                                       )

admin.site.register(CostumUser,CostumUserAdmin)
