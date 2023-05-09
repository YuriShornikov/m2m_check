from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleTag, Tag
#
class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True:
                count += 1
            if count == 0:
                raise ValidationError('Добавьте главный тег')
            if count > 1:
                raise ValidationError('mistake')

        
        return super().clean()

class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline]
    # pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass