from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'last_login', 'is_active', 'date_joined')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    # Burada Admin panelindeki kullanıcı düzenleme sayfasındaki alanlar
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Yeni kullanıcı oluşturma ekranında hangi alanların olacağını belirleyin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

    # Bu alanları kullanmıyorsanız boş bırakabilirsiniz
    filter_horizontal = ()
    list_filter = ()


admin.site.register(Account, AccountAdmin)