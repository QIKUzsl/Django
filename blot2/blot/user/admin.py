from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'name']
    list_filter = ['id']
    list_per_page = 2
    fields = ['name', 'age']
    actions_on_top = True
    # actions_on_bottom = True


class UserArticle(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'user_id']
    list_filter = ['id']
    list_per_page = 2


admin.site.register(models.Article, UserArticle)
admin.site.register(models.Users, UserAdmin)