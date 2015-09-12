from django.contrib import admin

from enlist import models

@admin.register(models.EmailConfirmation)
class EmailConfirmationAdmin(admin.ModelAdmin):
    list_display = ('account', 'email', 'verified',)
