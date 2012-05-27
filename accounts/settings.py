# -*- coding: utf-8 -*-
from django.conf import settings 

REGISTER_FORM = getattr(settings, "REGISTRATION_REGISTER_FORM", "accounts.forms.BaseRegistrationForm")
