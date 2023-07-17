# Melakukan Model Filter

import django_filters
from django_filters import DateFilter, CharFilter

from .models import * # Mengambil semua model

class Kecamatan_br_1_Filter(django_filters.FilterSet):
    
    note = CharFilter(field_name='note', lookup_expr='icontains')


    class Meta:
        model   = Kecamatan_br1
        fields  = '__all__'
        