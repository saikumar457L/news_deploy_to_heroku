from django.contrib import admin

from .models import Article,Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user","date"]
    list_filter = ["user","date"]

class CommentInline(admin.StackedInline):
    model = Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","user","date"]
    list_filter  = ["user","date"]
    inlines  = [CommentInline]
