from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, FormLogin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Profil_Admin

# =============================== BARIS HOME PAGE ===============================
from .models import Kecamatan_br1, Kecamatan_br2, AgendaBaru
from .filters import Kecamatan_br_1_Filter
import plotly.graph_objects as go
@login_required(login_url='login-page')
def Admin(request):
    agenda = AgendaBaru.objects.all()
    
    balita_br2 = Kecamatan_br2.objects.all()
    balita_br1 = Kecamatan_br1.objects.all()

    # Menghitung Jumlah Laki dan Perempuan
    L_total_balita_br_1 = balita_br1.filter(jk='L').count()
    P_total_balita_br_1 = balita_br1.filter(jk='P').count()
    
    L_total_balita_br_2 = balita_br2.filter(jk='L').count()
    P_total_balita_br_2 = balita_br2.filter(jk='P').count()
    l_P_Br_gab = L_total_balita_br_1 + P_total_balita_br_1 + L_total_balita_br_2 + P_total_balita_br_2

    # Menghitung Jumlah TB_U 'Tinggi'
    tb_tinggi_br_1 = balita_br1.filter(tb_u='Tinggi').count()
    tb_tinggi_br_2 = balita_br2.filter(tb_u='Tinggi').count()
    tb_tinggi_gab = tb_tinggi_br_1 + tb_tinggi_br_2
    
    # Menghitung Jumlah TB_U 'Normal'
    tb_normal_br_1 = balita_br1.filter(tb_u='Normal').count()
    tb_normal_br_2 = balita_br2.filter(tb_u='Normal').count()
    tb_normal_br_gab = tb_normal_br_1 + tb_normal_br_2

    # Menghitung Jumlah TB_U 'Pendek'
    tb_pendek_br_1 = balita_br1.filter(tb_u='Pendek').count()
    tb_pendek_br_2 = balita_br2.filter(tb_u='Pendek').count()
    tb_pendek_br_gab = tb_pendek_br_1 + tb_pendek_br_2

    # Menghitung Jumlah TB_U 'Sangat Pendek'
    tb_sangat_pendek_br_1 = balita_br1.filter(tb_u='Sangat Pendek').count()
    tb_sangat_pendek_br_2 = balita_br2.filter(tb_u='Sangat Pendek').count()
    tb_sangat_pendek_br_gab = tb_sangat_pendek_br_1 + tb_sangat_pendek_br_2

    
    labels = ['Tinggi','Normal','Pendek','Sangat Pendek']
    values = [tb_tinggi_gab, tb_normal_br_gab, tb_pendek_br_gab, tb_sangat_pendek_br_gab]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                             insidetextorientation='radial'
                            )])
# Change the bar mode
    a = fig.to_html(default_height=320, default_width=320)
    context  = {
        'name' : 'Halaman Admin',
        'agenda' : agenda,
        'l_P_Br_gab' : l_P_Br_gab,
        'tb_tinggi_gab' : tb_tinggi_gab,
        'tb_normal_br_gab' : tb_normal_br_gab,
        'tb_pendek_br_gab' : tb_pendek_br_gab,
        'tb_sangat_pendek_br_gab' : tb_sangat_pendek_br_gab,
        'graph': a,
    }
    return render(request, 'accounts/1_dashboard.html', context)

#==================================== BARIS MENU AGENDA =========================
from .forms import Agenda_baru_form
from .models import AgendaBaru

@login_required(login_url='login-page')
def Tambah_Agenda(request):
    form = Agenda_baru_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.error(request, "Agenda anda berhasil ditambahkan")
            return redirect('admin-page')
        else:
            messages.error(request, "You already have that project sample!")
        
    context  = {
        'form' : form,
    }
    return render(request, 'accounts/1_agenda_tambah.html', context)

# Delete Agenda
@login_required(login_url='login-page')
def Delete_Agenda(request, pk):
    try:
        agenda = AgendaBaru.objects.get(pk=pk)
        agenda.delete()
        messages.error(request, "Agenda berhasil dihapus")
        return redirect('admin-page')
    except:
        return redirect('admin-page')
    

#==================================== BARIS LOGIN & REGISTER =========================

# Membuat Form untuk registrasi
def registerPage(request):
    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
          form.save()
          messages.success(request, 'Registrasi Succes')
          return redirect("login-page")
        else:
          messages.error(request, 'Registrasi gagal')
    context  = {
        'form' : form,
    }
    return render(request, 'accounts/4_register.html', context)


# Mengecek Form untuk login
from django.contrib import messages
def loginPage(request):
    form = FormLogin()
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)


        if user is not None : 
            login(request, user)
            messages.success(request, 'Login Berhasil')
            return redirect('admin-page')
        else :
             # Eror Handling
             messages.warning(request, 'Username Atau Password Salah !!!')

    context = {'form':form}
    return render(request, 'accounts/4_login.html', context)

#==================================== MENU DATABASE =========================

@login_required(login_url='login-page')
def menu_database(request):
    context = {
        'name' : 'Data'
    }
    return render(request, 'accounts/2_menu_data.html', context)


#==================================== BARIS DATABASE BR 2 =========================
from .models import Kecamatan_br2
@login_required(login_url='login-page')
def database_br_2(request):

    data_br_2 = Kecamatan_br2.objects.all()
    context  = {
        'data_br_2' : data_br_2,
    }
    return render(request, 'database_br_2/2_data.html', context)

# Menambahkan Data
from . forms import BR_2_form
@login_required(login_url='login-page')
def AddDatabase_br_2(request):
    form = BR_2_form()
    if request.method == 'POST':
        form = BR_2_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('/database_br_2/')
        else:
            print ('Form Invalid')
    context  = {
        'form' : form,
    }
    return render(request, 'database_br_2/2_add_data.html', context)

@login_required(login_url='login-page')
def DeleteDatabase_br_2(request,pk):
    data_delete_br_2 = Kecamatan_br2.objects.get(id=pk)
    data_delete_br_2.delete()
    messages.success(request, 'Data berhasil dihapus')
    return redirect('/database_br_2/')
    
@login_required(login_url='login-page')
def EditDatabase_br_2(request, pk):
    data_edit_br_2 = Kecamatan_br2.objects.get(id=pk)
    form = BR_2_form(instance=data_edit_br_2)
    if request.method == 'POST':
        form = BR_2_form(request.POST, instance=data_edit_br_2)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diubah')
            return redirect('/database_br_2/')
        else:
            print ('Form Invalid')
    context  = {
        'form' : form,
        'edit_br_2' : data_edit_br_2,
    }
    return render(request, 'database_br_2/2_edit_data.html', context)



#==================================== BARIS DATABASE BR 1 =========================
from .models import Kecamatan_br1
@login_required(login_url='login-page')
def database_br_1(request):

    data_br_1 = Kecamatan_br1.objects.all()
    context  = {
        'data_br_1' : data_br_1,
    }
    return render(request, 'database_br_1/2_data.html', context)


# Menambahkan Data 
from . forms import BR_1_form
@login_required(login_url='login-page')
def AddDatabase_br_1(request):
    form = BR_1_form()
    if request.method == 'POST':
        form = BR_1_form(request.POST)
        if form.is_valid():
            form.save()
            # create a messages
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('/database_br_1/')
        else:
            print ('Form Invalid')
    context  = { 'form' : form }
    return render(request, 'database_br_1/2_add_data.html', context)


@login_required(login_url='login-page')
def DeleteDatabase_br_1(request, pk):
    data_delete_br_1 = Kecamatan_br1.objects.get(id=pk)
    data_delete_br_1.delete()
    # create a messages
    messages.success(request, 'Data berhasil dihapus')
    return redirect('/database_br_1/')
    

@login_required(login_url='login-page')
def EditDatabase_br_1(request, pk):
    data_edit_br_1 = Kecamatan_br1.objects.get(id=pk)
    form           = BR_1_form(instance=data_edit_br_1)
    if request.method == 'POST':
        form = BR_1_form(request.POST, instance=data_edit_br_1)
        if form.is_valid():
            form.save()
            # create a messages
            messages.success(request, 'Data berhasil diubah')
            return redirect('/database_br_1/')
        else:
            print ('Form Invalid')
    context  = {
        'form' : form,
        'edit_br_1' : data_edit_br_1,
        }
    return render(request, 'database_br_1/2_edit_data.html', context)

#==================================== BARIS DATABASE DATA TRAINING =========================
from .models import Data_Training
@login_required(login_url='login-page')
def data_training(request):

    data_training_fix = Data_Training.objects.all()
    context  = {
        'data_training_fix' : data_training_fix,
    }
    return render(request, 'data_training/2_data_training.html', context)

# Menambahkan Data
from . forms import Data_Training_form
@login_required(login_url='login-page')
def add_data_training(request):
    form = Data_Training_form()
    if request.method == 'POST':
        form = Data_Training_form(request.POST)
        if form.is_valid():
            form.save()
            # create a messages
            messages.success(request, 'Data training berhasil ditambahkan')
            return redirect('/data_training/')
        else:
            print ('Form Invalid')
    context  = {
        'form' : form,
        }
    return render(request, 'data_training/2_add_data_training.html', context)

# Menghapus Data
@login_required(login_url='login-page')
def DeleteDataTraining(request,pk):
    data_training_delete = Data_Training.objects.get(id=pk)
    data_training_delete.delete()
    # create a messages
    messages.success(request, 'Data training berhasil dihapus')
    return redirect('/data_training/')

# Mengedit Data
@login_required(login_url='login-page')
def EditDataTraining(request,pk):
    data_training_edit = Data_Training.objects.get(id=pk)
    form               = Data_Training_form(instance=data_training_edit)
    if request.method == 'POST':
        form = Data_Training_form(request.POST, instance=data_training_edit)
        if form.is_valid():
            form.save()
            # create a messages
            messages.success(request, 'Data training berhasil diubah')
            return redirect('/data_training/')
        else:
            print ('Form Invalid')
    context = {
        'form' : form,
        'data_training_edit' : data_training_edit,
    }
    return render(request, 'data_training/2_edit_data_training.html', context)


#==================================== BARIS DATABASE DATA TESTING =========================
from .models import Data_Testing
@login_required(login_url='login-page')
def data_testing(request):

    data_testing_fix = Data_Testing.objects.all()
    context  = {
        'data_testing_fix' : data_testing_fix,
    }
    return render(request, 'data_testing/2_data_testing.html', context)

# Menambahkan Data
from . forms import Data_Testing_form
@login_required(login_url='login-page')
def add_data_testing(request):
    form = Data_Testing_form()
    if request.method == 'POST':
        form = Data_Testing_form(request.POST)
        if form.is_valid():
            form.save()
            # create a messages
            messages.success(request, 'Data Testing berhasil ditambahkan')
            return redirect('/data_testing/')
        else:
            print ('Form Invalid')
    context  = {
        'form' : form,
        }
    return render(request, 'data_testing/2_add_data_testing.html', context)

# Menghapus Data
@login_required(login_url='login-page')
def DeleteDataTesting(request,pk):
    data_testing_delete = Data_Testing.objects.get(id=pk)
    data_testing_delete.delete()
    # create messages
    messages.success(request, 'Data Testing berhasil dihapus')
    return redirect('/data_testing/')

# Mengedit Data
@login_required(login_url='login-page')
def EditDataTesting(request,pk):
    data_testing_edit = Data_Testing.objects.get(id=pk)
    form               = Data_Testing_form(instance=data_testing_edit)
    if request.method == 'POST':
        form = Data_Testing_form(request.POST, instance=data_testing_edit)
        if form.is_valid():
            form.save()
            # create a messages
            messages.success(request, 'Data Testing berhasil diubah')
            return redirect('/data_testing/')
        else:
            print ('Form Invalid')
    context = {
        'form' : form,
        'data_testing_edit' : data_testing_edit,
    }
    return render(request, 'data_testing/2_edit_data_testing.html', context)


@login_required(login_url='login-page')
def menu_prediksi(request):
    context = {
        'name' : 'Prediksi'
    }
    return render(request, 'accounts/2_menu_check_app.html', context)



#==================================== BARIS BARIS CHECK STUNTING DENGENA MODEL PYTHON ========================
from joblib import load
import numpy as np
model = load('./savedModels/model_aplikasi.joblib')
@login_required(login_url='login-page')
def Prediksi(request):
    if request.method == 'POST':

        nama = request.POST['nama']
        jenis_kelamin = request.POST['jenis_kelamin']
        if jenis_kelamin == 'laki-laki':
            jenis_kelamin_fix = 1
        elif jenis_kelamin == 'perempuan':
            jenis_kelamin_fix = 0

        status_ekonomi = request.POST['status_ekonomi']
        if status_ekonomi == 'Kurang Mampu':
            status_ekonomi_fix = 1
        elif status_ekonomi == 'Mampu':
            status_ekonomi_fix = 0

        usia_ukur = request.POST['usia_ukur']
        if usia_ukur == 'Kurang Dari 3 Tahun':
            usia_ukur_fix = 2
        elif usia_ukur == '3 Tahun':
            usia_ukur_fix = 0
        elif usia_ukur == 'Lebih Dari 3 Tahun':
            usia_ukur_fix = 1

        bb_u = request.POST['bb_u']
        if bb_u == 'BB Sangat Kurang':
            bb_u_fix = 2
        elif bb_u == 'BB Kurang':
            bb_u_fix = 0
        elif bb_u == 'BB Normal':
            bb_u_fix = 1

        tb_u = request.POST['tb_u']
        if tb_u == 'TB Sangat Pendek':
            tb_u_fix = 2
        elif tb_u == 'TB Pendek':
            tb_u_fix = 0
        elif tb_u == 'TB Normal':
            tb_u_fix = 1
        elif tb_u == 'TB Tinggi':
            tb_u_fix = 3

        status_gizi = request.POST['status_gizi']
        if status_gizi == 'Gizi Baik':
            status_gizi_fix = 1
        elif status_gizi == 'Gizi Kurang':
            status_gizi_fix = 0

        akurasi = '96%'

        user = ([[jenis_kelamin_fix, status_ekonomi_fix, usia_ukur_fix, bb_u_fix, tb_u_fix, status_gizi_fix]])
        user_can = np.array(user, dtype=float)
        nbc_pred = model.predict(user_can)
        # messages
        messages.error(request, "Prediksi Berhasil")
        if nbc_pred == ([0]):
            nbc_pred = "Balita Memiliki Potensi Stunting Stunting"
        elif nbc_pred == ([1]):
            nbc_pred = "Balita Normal / Tidak Stunting"
        else :
            nbc_pred = "Balita Stunting"
        context  = {
            'nama' : nama,
            'jenis_kelamin' : jenis_kelamin,
            'status_ekonomi' : status_ekonomi,
            'usia_ukur' : usia_ukur,
            'akurasi' : akurasi,
            'status_gizi' : status_gizi,
            'bb_u' : bb_u,
            'tb_u' : tb_u,
            'status_gizi' : status_gizi,
            'result' : nbc_pred,
            }
        return render(request, 'accounts/3_check_app.html', context)
    return render(request, 'accounts/3_check_app.html')

#==================================== BARIS BARIS CHECK STUNTING DENGAN DEVELOP ========================
@login_required(login_url='login-page')
def prediksi_stunting_develop(request):
    if request.method == 'POST':
        # Mendapatkan nilai input dari form
        nama = request.POST.get('nama')
        jenis_kelamin = request.POST.get('jenis_kelamin')
        status_ekonomi = request.POST.get('status_ekonomi')
        usia_ukur = request.POST.get('usia_ukur')
        berat_badan_umur = request.POST.get('bb_u')
        tinggi_badan_umur = request.POST.get('tb_u')
        status_gizi = request.POST.get('status_gizi')

        # Deklarasi Menghitung jumlah variabel Kelas Lebel/Jumlah Data Training
        p_y_tidak = 0.935
        p_y_stunting = 0.935
        p_y_potensi = 0.935

        # Deklarasi Menghitung jumlah variabel kelas Jenis Kelamin/Label
        p_jenis_kelamin_l_tidak = 0.522
        p_jenis_kelamin_l_stunting = 0.560
        p_jenis_kelamin_l_potensi = 0.560
        p_jenis_kelamin_p_tidak = 0.478
        p_jenis_kelamin_p_stunting = 0.440
        p_jenis_kelamin_p_potensi = 0.442

        # Deklarasi Menghitung jumlah variabel kelas Status Ekonomi/Label
        p_status_ekonomi_mampu_tidak = 0.973
        p_status_ekonomi_mampu_stunting = 0.84
        p_status_ekonomi_mampu_potensi = 0.849
        p_status_ekonomi_kurang_mampu_tidak = 0.015
        p_status_ekonomi_kurang_mampu_stunting = 0.16
        p_status_ekonomi_kurang_mampu_potensi = 0.151

        # Deklarasi Menghitung jumlah variabel kelas Usia Ukur/Label
        p_usia_ukur_3_tahun_tidak = 0.242
        p_usia_ukur_3_tahun_stunting = 0.36
        p_usia_ukur_3_tahun_potensi = 0.302
        p_usia_ukur_lebih_3_tahun_tidak = 0.289
        p_usia_ukur_lebih_3_tahun_stunting = 0.24
        p_usia_ukur_lebih_3_tahun_potensi = 0.291
        p_usia_ukur_kurang_3_tahun_tidak = 0.468
        p_usia_ukur_kurang_3_tahun_stunting = 0.4
        p_usia_ukur_kurang_3_tahun_potensi = 0.407

        # Deklarasi Menghitung jumlah variabel kelas BB/U/Label
        p_berat_badan_normal_tidak = 0.991
        p_berat_badan_normal_stunting = 0.04
        p_berat_badan_normal_potensi = 0.406
        p_berat_badan_kurang_tidak = 0.009
        p_berat_badan_kurang_stunting = 0.76
        p_berat_badan_kurang_potensi = 0
        p_berat_badan_sangat_kurang_tidak = 0
        p_berat_badan_sangat_kurang_stunting = 0.2
        p_berat_badan_sangat_kurang_potensi = 0

        # Deklarasi Menghitung jumlah variabel kelas TB/U/Label
        p_tinggi_badan_normal_tidak = 0.966
        p_tinggi_badan_normal_stunting = 0
        p_tinggi_badan_normal_potensi = 0.139
        p_tinggi_badan_tinggi_tidak = 0.001
        p_tinggi_badan_tinggi_stunting = 0
        p_tinggi_badan_tinggi_potensi = 0
        p_tinggi_badan_pendek_tidak = 0.001
        p_tinggi_badan_pendek_stunting = 0.44
        p_tinggi_badan_pendek_potensi = 0.767
        p_tinggi_badan_sangat_pendek_tidak = 0.001
        p_tinggi_badan_sangat_pendek_stunting = 0.56
        p_tinggi_badan_sangat_pendek_potensi = 0.093

        # Deklarasi Menghitung jumlah variabel kelas BB/TB/Label
        p_status_gizi_baik_tidak = 0.996
        p_status_gizi_baik_stunting = 0.12
        p_status_gizi_baik_potensi = 0.848
        p_status_gizi_kurang_tidak = 0.004
        p_status_gizi_kurang_stunting = 0.88
        p_status_gizi_kurang_potensi = 0.151

        # Deklarasi variabel probabilitas dan hasil prediksi
        prob_tidak_stunting = 0
        prob_stunting = 0
        prob_potensi_stunting = 0
        hasil = ''

        # Menghitung Probabilitas Jenis Kelamin
        if jenis_kelamin == 'laki-laki':
            p_jenis_kelamin_tidak = p_jenis_kelamin_l_tidak
            p_jenis_kelamin_stunting = p_jenis_kelamin_l_stunting
            p_jenis_kelamin_potensi = p_jenis_kelamin_l_potensi
        elif jenis_kelamin == 'perempuan' :
            p_jenis_kelamin_tidak = p_jenis_kelamin_p_tidak
            p_jenis_kelamin_stunting = p_jenis_kelamin_p_stunting
            p_jenis_kelamin_potensi = p_jenis_kelamin_p_potensi

        # Menghitung Probabilitas Status Ekonomi
        if status_ekonomi == 'Mampu':
            p_status_ekonomi_tidak = p_status_ekonomi_mampu_tidak
            p_status_ekonomi_stunting = p_status_ekonomi_mampu_stunting
            p_status_ekonomi_potensi = p_status_ekonomi_mampu_potensi
        elif status_ekonomi == 'Kurang Mampu':
            p_status_ekonomi_tidak = p_status_ekonomi_kurang_mampu_tidak
            p_status_ekonomi_stunting = p_status_ekonomi_kurang_mampu_stunting
            p_status_ekonomi_potensi = p_status_ekonomi_kurang_mampu_potensi

        # Menghitung Probabilitas Usia Ukur
        if usia_ukur == '3 Tahun':
            p_usia_ukur_tidak = p_usia_ukur_3_tahun_tidak
            p_usia_ukur_stunting = p_usia_ukur_3_tahun_stunting
            p_usia_ukur_potensi = p_usia_ukur_3_tahun_potensi
        elif usia_ukur == 'Lebih Dari 3 Tahun':
            p_usia_ukur_tidak = p_usia_ukur_lebih_3_tahun_tidak
            p_usia_ukur_stunting = p_usia_ukur_lebih_3_tahun_stunting
            p_usia_ukur_potensi = p_usia_ukur_lebih_3_tahun_potensi
        elif usia_ukur == 'Kurang Dari 3 Tahun':
            p_usia_ukur_tidak = p_usia_ukur_kurang_3_tahun_tidak
            p_usia_ukur_stunting = p_usia_ukur_kurang_3_tahun_stunting
            p_usia_ukur_potensi = p_usia_ukur_kurang_3_tahun_potensi

        # Menghitung Probabilitas BB/U
        if berat_badan_umur == 'BB Normal':
            p_berat_badan_umur_tidak = p_berat_badan_normal_tidak
            p_berat_badan_umur_stunting = p_berat_badan_normal_stunting
            p_berat_badan_umur_potensi = p_berat_badan_normal_potensi
        elif berat_badan_umur == 'BB Kurang':
            p_berat_badan_umur_tidak = p_berat_badan_kurang_tidak
            p_berat_badan_umur_stunting = p_berat_badan_kurang_stunting
            p_berat_badan_umur_potensi = p_berat_badan_kurang_potensi
        elif berat_badan_umur == 'BB Sangat Kurang':
            p_berat_badan_umur_tidak = p_berat_badan_sangat_kurang_tidak
            p_berat_badan_umur_stunting = p_berat_badan_sangat_kurang_stunting
            p_berat_badan_umur_potensi = p_berat_badan_sangat_kurang_potensi

        # Menghitung Probabilitas TB/U
        if tinggi_badan_umur == 'TB Normal':
            p_tinggi_badan_umur_tidak = p_tinggi_badan_normal_tidak
            p_tinggi_badan_umur_stunting = p_tinggi_badan_normal_stunting
            p_tinggi_badan_umur_potensi = p_tinggi_badan_normal_potensi
        elif tinggi_badan_umur == 'TB Tinggi':
            p_tinggi_badan_umur_tidak = p_tinggi_badan_tinggi_tidak
            p_tinggi_badan_umur_stunting = p_tinggi_badan_tinggi_stunting
            p_tinggi_badan_umur_potensi = p_tinggi_badan_tinggi_potensi
        elif tinggi_badan_umur == 'TB Pendek':
            p_tinggi_badan_umur_tidak = p_tinggi_badan_pendek_tidak
            p_tinggi_badan_umur_stunting = p_tinggi_badan_pendek_stunting
            p_tinggi_badan_umur_potensi = p_tinggi_badan_pendek_potensi
        elif tinggi_badan_umur == 'TB Sangat Pendek':
            p_tinggi_badan_umur_tidak = p_tinggi_badan_sangat_pendek_tidak
            p_tinggi_badan_umur_stunting = p_tinggi_badan_sangat_pendek_stunting
            p_tinggi_badan_umur_potensi = p_tinggi_badan_sangat_pendek_potensi

        # Menghitung Probabilitas BB/TB
        if status_gizi == 'Gizi Baik':
            p_status_gizi_tidak = p_status_gizi_baik_tidak
            p_status_gizi_stunting = p_status_gizi_baik_stunting
            p_status_gizi_potensi = p_status_gizi_baik_potensi
        elif status_gizi == 'Gizi Kurang':
            p_status_gizi_tidak = p_status_gizi_kurang_tidak
            p_status_gizi_stunting = p_status_gizi_kurang_stunting
            p_status_gizi_potensi = p_status_gizi_kurang_potensi

        # Menghitung probabilitas untuk setiap label
        prob_tidak_stunting = p_jenis_kelamin_tidak * p_status_ekonomi_tidak * p_usia_ukur_tidak * p_berat_badan_umur_tidak * p_tinggi_badan_umur_tidak * p_status_gizi_tidak * p_y_tidak
        prob_stunting = p_jenis_kelamin_stunting * p_status_ekonomi_stunting * p_usia_ukur_stunting * p_berat_badan_umur_stunting * p_tinggi_badan_umur_stunting * p_status_gizi_stunting * p_y_stunting
        prob_potensi_stunting = p_jenis_kelamin_potensi * p_status_ekonomi_potensi * p_usia_ukur_potensi * p_berat_badan_umur_potensi * p_tinggi_badan_umur_potensi * p_status_gizi_potensi * p_y_potensi

        messages.error(request, "Prediksi Berhasil")
        
        # Menentukan hasil prediksi
        if prob_tidak_stunting > prob_stunting and prob_tidak_stunting > prob_potensi_stunting:
            hasil = 'Balita Normal / Tidak Stunting'
        elif prob_stunting > prob_tidak_stunting and prob_stunting > prob_potensi_stunting:
            hasil = 'Balita Stunting'
        else:
            hasil = 'Balita Memiliki Potensi Stunting Stunting'

        akurasi = '96%'
        # Menyiapkan data untuk dikirim ke template
        context = {
            'nama': nama,
            'jenis_kelamin': jenis_kelamin,
            'status_ekonomi': status_ekonomi,
            'usia_ukur': usia_ukur,
            'berat_badan_umur': berat_badan_umur,
            'tinggi_badan_umur': tinggi_badan_umur,
            'status_gizi': status_gizi,
            'hasil': hasil,
            'akurasi' : akurasi
        }

        return render(request, 'accounts/3_check_app_develop.html', context)
    return render(request, 'accounts/3_check_app_develop.html')




# Menampilkan Data Hasil Prediksi Berdasarkan Database
from .forms import DataForm
from .models import Data_Prediksi
@login_required(login_url='login-page')
def Prediksi_data_hasil(request):
    predicted_stunted = Data_Prediksi.objects.all()
    context = {
        'predicted_stunted': predicted_stunted
    }
    return render(request, 'data_hasil_prediksi/2_data_hasil_prediksi.html', context)

@login_required(login_url='login-page')
def rekap_prediksi(request):
    form = DataForm()
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            # create messages
            messages.success(request, "Data Prediksi Berhasil Disimpan")
            return redirect('rekapan-prediksi-page')
        else:
            print('form Invalid')
    context = {
        'form': form,
    }
    return render(request, 'data_hasil_prediksi/2_data_prediksi.html', context)

# Menghapus Data
@login_required(login_url='login-page')
def DeleteDatarekap(request,pk):
    data_rekap_delete = Data_Prediksi.objects.get(id=pk)
    data_rekap_delete.delete()
    # create messages
    messages.success(request, "Data Prediksi Berhasil Dihapus")
    return redirect('rekapan-prediksi-page')

#==================================== BARIS STUNTING INFO =========================
@login_required(login_url='login-page')
def StuntingInfo(request):
    
    context  = {
        'name' : 'Data',
    }
    return render(request, 'accounts/5_content.html', context)

#==================================== BARIS STUNTING INFO =========================
@login_required(login_url='login-page')
def StuntingInfoDevelop(request):
    
    context  = {
        'name' : 'Develop',
    }
    return render(request, 'accounts/6_info_perhitungan.html', context)




