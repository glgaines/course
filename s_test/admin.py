# -*- coding: utf-8 -*-
from django.contrib import admin

from django.db import models
from django.forms import TextInput


from s_test.models import (Test, TestQuestion, TestAnswer, TestScale, TestResult, )



class TestScaleInline(admin.TabularInline):
    model = TestScale
    fieldsets = [
        (None, {
            'fields': ['comment', 'start', 'end', ], 'classes': ['collapse']
        }),
    ]

class AdminTest(admin.ModelAdmin):
    #list_display = ('name', 'get_comments', 'pages', )
    #list_editable = ('pages', )
    fieldsets = [
        (None, {
            'fields': ['name', 'pages', 'comments']
        }),
    ]
    inlines = [
        TestScaleInline,
        ]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'150'})},
        }
admin.site.register(Test, AdminTest)

class TestAnswerInline(admin.TabularInline):
    model = TestAnswer
    fieldsets = [
        (None, {
            'fields': ['content', 'weight',], 'classes': ['collapse']
        }),
    ]

class AdminTestQuestion(admin.ModelAdmin):
    list_display = ('title', 'get_comments', 'position', )
    list_editable = ('position', )
    list_filter = ('test__name', )
    inlines = [
        TestAnswerInline,
        ]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'150'})},
        }

admin.site.register(TestQuestion, AdminTestQuestion)

class AdminTestResult(admin.ModelAdmin):
    pass
admin.site.register(TestResult, AdminTestResult)