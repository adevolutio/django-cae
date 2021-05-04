# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _


class Section(models.Model):
    code = models.CharField(_('Código'), max_length=1, primary_key=True)
    name = models.CharField(_('Designação'), max_length=128)

    def __str__(self):
        return "%s: %s" % (self.code, self.name)

    class Meta:
        verbose_name = _('Secção')
        verbose_name_plural = _('Secções')
        db_table = 'cae_section'


class Division(models.Model):
    code = models.SmallIntegerField(_('Código'), primary_key=True)
    name = models.CharField(_('Designação'), max_length=128)
    section = models.ForeignKey(Section, verbose_name=_('Secção'), on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.formatted_code, self.name)

    class Meta:
        verbose_name = _('Divisão')
        verbose_name_plural = _('Divisões')
        db_table = 'cae_division'

    @property
    def formatted_code(self):
        return "%02d" % self.code


class CAE(models.Model):
    level = models.SmallIntegerField(_('Nível'))
    code = models.IntegerField(_('Código'))
    name = models.CharField(_('Designação'), max_length=255)

    def __str__(self):
        return "%s - %s" % (self.formatted_code, self.name)

    class Meta:
        verbose_name = _('CAE')
        verbose_name_plural = _('CAE\'s')
        db_table = 'cae_cae'
        unique_together = ('level', 'code')

    @property
    def formatted_code(self):
        if self.level == 3:
            return "%03d" % self.code
        elif self.level == 4:
            return "%04d" % self.code
        else:
            return "%05d" % self.code
