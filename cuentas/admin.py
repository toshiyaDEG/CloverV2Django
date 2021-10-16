from django.contrib import admin

from .models import Account


# class AccountAdmin(admin.ModelAdmin):
#     list_display = ("username", "email")

admin.site.register(Account)