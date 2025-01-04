# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Device_Info(models.Model):

    #__Device_Info_FIELDS__
    id = models.TextField(max_length=255, null=True, blank=True)

    #__Device_Info_FIELDS__END

    class Meta:
        verbose_name        = _("Device_Info")
        verbose_name_plural = _("Device_Info")


class Holiday(models.Model):

    #__Holiday_FIELDS__
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    day = models.TextField(max_length=255, null=True, blank=True)
    occassion = models.TextField(max_length=255, null=True, blank=True)
    type = models.TextField(max_length=255, null=True, blank=True)
    location = models.TextField(max_length=255, null=True, blank=True)

    #__Holiday_FIELDS__END

    class Meta:
        verbose_name        = _("Holiday")
        verbose_name_plural = _("Holiday")



#__MODELS__END
