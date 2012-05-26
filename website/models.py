# -*- coding: utf-8 -*-
# models.py
from django.db import models

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^common\.fields\.MultiEmailField"])

import re
from django.db import models
from django.core.validators import validate_email
from south.modelsinspector import add_introspection_rules

def emails_list(value):
    return filter(lambda x: bool(x.strip()), re.split(r'[,|;]?\s?', value or ''))

class MultiEmailField(models.CharField):
    def validate(self, value, model_instance):
        super(MultiEmailField, self).validate(value, model_instance)
        for email in emails_list(value):
            validate_email(email)


add_introspection_rules([], ["^common\.fields\.MultiEmailField"])

class Settings(models.Model):
    project = models.CharField(u'Название проекта', max_length=255)
    email = MultiEmailField(u'Email для писем о тестировании', max_length=255,
        help_text=u'''Можете вставить несколько email, разделив их запятой''')

    def __unicode__(self):
        return u'настройки'

    class Meta:
        verbose_name = u'настройки'
        verbose_name_plural = u'настройки'