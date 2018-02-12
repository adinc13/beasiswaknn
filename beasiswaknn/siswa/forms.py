from django import forms

from beasiswaknn.siswa.models import Siswa, SiswaBaru


class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12', 'placeholder': 'Name'}),
            'x1': forms.Select(attrs={'class': 'form-control'}),
            'x2': forms.Select(attrs={'class': 'form-control'}),
            'x3': forms.Select(attrs={'class': 'form-control'}),
            'x4': forms.Select(attrs={'class': 'form-control'}),
            'x5': forms.Select(attrs={'class': 'form-control'}),
            'x6': forms.Select(attrs={'class': 'form-control'}),
            'x7': forms.Select(attrs={'class': 'form-control'}),
            'x8': forms.Select(attrs={'class': 'form-control'}),
            'x9': forms.Select(attrs={'class': 'form-control'}),
        }


class SiswaBaruForm(forms.ModelForm):
    k = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Nilai K',
        'class': 'form-control input-white'
    }))

    class Meta:
        model = SiswaBaru
        fields = ('name', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'k')
        exclude = ('beasiswa',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12', 'placeholder': 'Name'}),
            'x1': forms.Select(attrs={'class': 'form-control'}),
            'x2': forms.Select(attrs={'class': 'form-control'}),
            'x3': forms.Select(attrs={'class': 'form-control'}),
            'x4': forms.Select(attrs={'class': 'form-control'}),
            'x5': forms.Select(attrs={'class': 'form-control'}),
            'x6': forms.Select(attrs={'class': 'form-control'}),
            'x7': forms.Select(attrs={'class': 'form-control'}),
            'x8': forms.Select(attrs={'class': 'form-control'}),
            'x9': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_k(self):
        k = self.cleaned_data.get('k')
        if k < 1:
            raise forms.ValidationError('Angka harus lebih dari 0')
        if k > Siswa.objects.count():
            raise forms.ValidationError('Angka maksimal {}'.format(Siswa.objects.count()))
        return k
