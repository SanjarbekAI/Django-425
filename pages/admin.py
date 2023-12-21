from django.contrib import admin
from pages.models import ContactModel, BlogModel, FeedbackModel, EmailModel


@admin.register(ContactModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']



@admin.register(BlogModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


@admin.register(FeedbackModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


@admin.register(EmailModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at']
