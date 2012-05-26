# -*- coding: utf-8 -*-
from django import forms

from s_test.models import TestAnswer, TestResult
def as_eul(self):
    return self._html_output(
        normal_row = u'<li%(html_class_attr)s><div class="FormLabel">%(label)s</div> <div class="FormField">%(field)s</div><div class="FormError">%(errors)s</div><div class="FormHelpText">%(help_text)s</div></li>',
        error_row = u'<li>%s</li>',
        row_ender = '</li>',
        help_text_html = u' %s',
        errors_on_separate_row = False)

forms.BaseForm.as_eul = as_eul
class TestAnswerRadioForm(forms.Form):
    answer = forms.ModelChoiceField(TestAnswer.objects.all(), label=u'', widget=forms.RadioSelect(), required=True)

    def __init__(self, queryset=None, *args, **kwargs):
        super(TestAnswerRadioForm, self).__init__(*args, **kwargs)
        self['answer'].field.empty_label = None
        if queryset:
            self['answer'].field.queryset = queryset

class TestAnswerCheckBoxForm(forms.Form):
    answer = forms.ModelMultipleChoiceField(TestAnswer.objects.all(), label=u'', widget=forms.CheckboxSelectMultiple())

    def __init__(self, queryset=None, *args, **kwargs):
        super(TestAnswerCheckBoxForm, self).__init__(*args, **kwargs)
        self['answer'].field.empty_label = None
        if queryset:
            self['answer'].field.queryset = queryset

class TestEmailForm(forms.ModelForm):
    class Meta:
        fields = ('email','fio','group')
        model = TestResult