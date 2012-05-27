# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from django import forms

from registration.forms import RegistrationFormUniqueEmail

attrs_dict = {'class': 'required'}

class ProfileRegistrationForm(RegistrationFormUniqueEmail):
    first_name = forms.RegexField(regex=ur'^[А-Яа-я\w.@+-]+$',
        max_length=30,
        widget=forms.TextInput(attrs=attrs_dict),
        label=_("first name"),
        error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})

    last_name = forms.RegexField(regex=ur'^[А-Яа-я\w.@+-]+$',
        max_length=30,
        widget=forms.TextInput(attrs=attrs_dict),
        label=_("last name"),
        error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})

class ProfileForm(forms.Form):
    first_name = forms.RegexField(regex=ur'^[А-Яа-я\w.@+-]+$',
        max_length=30,
        widget=forms.TextInput(attrs=attrs_dict),
        label=_("first name"),
        error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})

    last_name = forms.RegexField(regex=ur'^[А-Яа-я\w.@+-]+$',
        max_length=30,
        widget=forms.TextInput(attrs=attrs_dict),
        label=_("last name"),
        error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    study_group = forms.CharField( label="Учебная группа")


