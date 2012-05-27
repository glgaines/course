# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    accepted_eula = models.BooleanField()
    is_student = models.BooleanField(u'Студент')
    study_group = models.CharField(u'Учебная группа', max_length=255, blank = True)

    def __unicode__(self):
        return u'%s - %s %s' % (self.user.username, self.user.first_name, self.user.last_name)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)