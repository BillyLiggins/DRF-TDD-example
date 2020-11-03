# Create your models here.
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _


class MyModel(models.Model):
    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("MyModel")
        verbose_name_plural = _("MyModels")

    def __unicode__(self):
        return smart_unicode(self.first_name)
