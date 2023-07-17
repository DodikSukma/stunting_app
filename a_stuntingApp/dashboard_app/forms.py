from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil_Admin

from django.forms import ModelForm

# ==================== MEMBUAT FORM REGISTRASI =======================
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# ==================== MEMBUAT FORM PROFIL USER =======================
class Profil_Admin(forms.ModelForm):
    class Meta:
        model = Profil_Admin
        fields = ["jabatan", "instansi"]


# ==================== MEMBUAT FORM login=======================
class FormLogin(forms.Form) :
    username = forms.CharField(
        widget= forms.TextInput(attrs={'class' : 'form-control', 'type' : 'text'}),
    )
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class' : 'form-control'}),
    )

# ==================== MEMBUAT FORM UNTUK DATABASE BR 1 ==================
from .models import Kecamatan_br1
class BR_1_form (ModelForm):
    class Meta :
        model = Kecamatan_br1 
        fields = '__all__' # Tambahkan Semua deklarasi Kolom disini all sama seperti menambahkan semua kolom

# ==================== MEMBUAT FORM UNTUK DATABASE BR 2 ==================
from .models import Kecamatan_br2
class BR_2_form (ModelForm):
    class Meta :
        model = Kecamatan_br2 
        fields = '__all__' # Tambahkan Semua deklarasi Kolom disini all sama seperti menambahkan semua kolom

# ==================== MEMBUAT FORM UNTUK DATA TRAINING ==================
from .models import Data_Training
class Data_Training_form (ModelForm):
    class Meta :
        model = Data_Training
        fields = '__all__' # Tambahkan Semua deklarasi Kolom disini all sama seperti menambahkan semua kolom

# ==================== MEMBUAT FORM UNTUK DATA TESTING ==================
from .models import Data_Testing
class Data_Testing_form (ModelForm):
    class Meta :
        model = Data_Testing
        fields = '__all__' # Tambahkan Semua deklarasi Kolom disini all sama seperti menambahkan semua kolom

     
# ==================== MEMBUAT FORM UNTUK REKAPAN PREDIKSI ==================
from .models import Data_Prediksi
class DataForm(forms.ModelForm):
    class Meta:
        model = Data_Prediksi
        fields = ['nama', 'jk', 'status_KM', 'usia_ukur', 'bb_u', 'tb_u', 'bb_tb']

from .models import AgendaBaru
class Agenda_baru_form(forms.ModelForm):
    class Meta:
        model = AgendaBaru
        fields = '__all__' # Tambahkan semua deklarasi sudah