from __future__ import unicode_literals

from django.db import models
from beasiswaknn.siswa.choices import KTP, KK, KELAS, PKH, KPS, SKTM, PANTI, LISTRIK, RANKING


class Siswa(models.Model):
    nomer = models.SmallIntegerField(null=True)
    name = models.CharField(max_length=100)
    x1 = models.SmallIntegerField()
    x2 = models.SmallIntegerField()
    x3 = models.SmallIntegerField()
    x4 = models.SmallIntegerField()
    x5 = models.SmallIntegerField()
    x6 = models.SmallIntegerField()
    x7 = models.SmallIntegerField()
    x8 = models.SmallIntegerField()
    x9 = models.SmallIntegerField()
    beasiswa = models.BooleanField()
    jarak = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'siswa_beasiswa'
        ordering = ['nomer']

    def __unicode__(self):
        return self.name


class SiswaBaru(models.Model):
    name = models.CharField(max_length=100)
    x1 = models.SmallIntegerField(choices=KTP)
    x2 = models.SmallIntegerField(choices=KK)
    x3 = models.SmallIntegerField(choices=KELAS)
    x4 = models.SmallIntegerField(choices=PKH)
    x5 = models.SmallIntegerField(choices=KPS)
    x6 = models.SmallIntegerField(choices=SKTM)
    x7 = models.SmallIntegerField(choices=PANTI)
    x8 = models.SmallIntegerField(choices=LISTRIK)
    x9 = models.SmallIntegerField(choices=RANKING)
    beasiswa = models.BooleanField(blank=True)

    class Meta:
        db_table = 'siswa_baru_beasiswa'
        ordering = ['-id']

    def __unicode__(self):
        return self.name
