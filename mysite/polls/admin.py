from django.contrib import admin

from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # 通过list_display来改变Questions的陈列方式
    list_display = (
        'question_text', 'pub_date', 'was_published_recently'
    )
    # 通过search_fields来增加搜索条
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)