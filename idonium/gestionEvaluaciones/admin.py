from django.contrib import admin

# Register your models here.
from .models import Test, Question, Option, Result

class OptionInline(admin.TabularInline):
    model = Option

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Test)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result)