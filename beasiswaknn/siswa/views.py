import csv
from math import sqrt

from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from beasiswaknn.siswa.forms import SiswaForm, SiswaBaruForm
from beasiswaknn.siswa.models import Siswa, SiswaBaru


def import_member(request):
    if 'csv_file' in request.FILES:
        csv_file = request.FILES['csv_file']

        datas = [row for row in csv.reader(csv_file.read().splitlines())]
        siswa_data = [dict(zip(datas[0], row)) for row in datas[1:]]
        for data in siswa_data:
            Siswa.objects.update_or_create(name=data.get('nama'), defaults=data)

    return render(request, 'import_siswa.html')


class SiswaList(ListView):
    model = Siswa
    template_name = 'list_data.html'
    context_object_name = 'data_siswa'
    paginate_by = 25
    queryset = Siswa.objects.all().order_by('jarak')

    def get_queryset(self):
        qs = Siswa.objects.all().order_by('jarak')
        keywords = self.request.GET.get('keywords', None)
        if keywords:
            qs = qs.filter(name__icontains=keywords)

        return qs


def DataBaru(request):
    data_training = list(Siswa.objects.all())
    form = SiswaBaruForm(request.POST or None)
    if request.POST and form.is_valid():
        testing = form.cleaned_data
        for data in data_training:
            x1 = (data.x1-testing['x1']) ** 2
            x2 = (data.x2-testing['x2']) ** 2
            x3 = (data.x3-testing['x3']) ** 2
            x4 = (data.x4-testing['x4']) ** 2
            x5 = (data.x5-testing['x5']) ** 2
            x6 = (data.x6-testing['x6']) ** 2
            x7 = (data.x7-testing['x7']) ** 2
            x8 = (data.x8-testing['x8']) ** 2
            x9 = (data.x9-testing['x9']) ** 2
            data.jarak = sqrt(x1+x2+x3+x4+x5+x6+x7+x8+x9)
            data.save()
        k = testing.pop('k')
        qs = Siswa.objects.all().order_by('jarak')[:k]
        list_target = []
        for siswa in qs:
            list_target.append(siswa.beasiswa)
        dapat = list_target.count(1)
        tidak = list_target.count(0)
        if dapat > tidak:
            testing['beasiswa'] = True
            messages.success(request, '{} MENDAPAT BEASISWA'.format(testing['name']))
            messages.success(request, 'Hasil K-NN : Dapat {} - Tidak Dapat {}'.format(dapat, tidak))
        else:
            testing['beasiswa'] = False
            messages.success(request, '{} TIDAK MENDAPAT BEASISWA'.format(testing['name']))
            messages.success(request, 'Hasil K-NN : Dapat {} - Tidak Dapat {}'.format(dapat, tidak))

        testing['nomer'] = Siswa.objects.last().nomer + 1

        Siswa.objects.create(**testing)

        return redirect('/siswa/')
    return render(request, 'input_data_baru.html', {'form': form, 'jumlah': Siswa.objects.all().count(),
                                                    'saran': Siswa.objects.all().count()/4})



# def import_data_baru(request):
#     if 'csv_file' in request.FILES:
#         csv_file = request.FILES['csv_file']
#
#         datas = [row for row in csv.reader(csv_file.read().splitlines())]
#         siswa_data = [dict(zip(datas[0], row)) for row in datas[1:]]
#         for data in siswa_data:
#
#             SiswaBaru.objects.update_or_create(name=data.get('nama'), defaults=data)
#
#     return render(request, 'import_siswa.html')


class SiswaBaruList(ListView):
    model = SiswaBaru
    template_name = 'list_data_baru.html'
    context_object_name = 'data_siswa'
    paginate_by = 25
    queryset = SiswaBaru.objects.all()

    def get_queryset(self):
        qs = SiswaBaru.objects.all()
        keywords = self.request.GET.get('keywords', None)
        if keywords:
            qs = qs.filter(name__icontains=keywords)

        return qs
