from django.contrib import admin

from beasiswaknn.siswa.models import Siswa, SiswaBaru
# Register your models here.

@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin):
    pass


@admin.register(SiswaBaru)
class SiswaBaruAdmin(admin.ModelAdmin):
    pass