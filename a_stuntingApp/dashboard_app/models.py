from django.db import models
from django.contrib.auth.models import User
from joblib import load

from sklearn.naive_bayes import GaussianNB                            # digunakan untuk metode NBC
from sklearn.model_selection import RepeatedStratifiedKFold           # digunakan untuk nilai k
from sklearn.metrics import classification_report,confusion_matrix    # digunakan untuk menhitung akurasi
from sklearn.metrics import f1_score, precision_score, recall_score   # digunakan untuk menghitung akurasu
from sklearn.model_selection import GridSearchCV                      # kombinasi yang berbeda dari semua hyperparameter  

# ========================= MEMBUAT PROFIL ADMIN ======================
class Profil_Admin(models.Model):
    nama            = models.ForeignKey(User, on_delete=models.CASCADE)
    jabatan         = models.CharField(max_length=200)
    instansi        = models.CharField(max_length=200)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama+ "\n" + self.jabatan
    
# ===================== MEMBUAT DATABASE KEECAMATAN BR 1 ================
class Kecamatan_br1(models.Model):
    JK = (
            ('L' , 'L'),
            ('P' , 'P'),
        )
    
    STKM = (
            ('Kurang Mampu' , 'Kurang Mampu'),
            ('Tidak' , 'Tidak'),
        )
    
    BB_U = (
            ('Berat Badan Normal' , 'Berat Badan Normal'),
            ('Kurang' , 'Kurang'),
            ('Risiko Lebih' , 'Risiko Lebih'),
            ('Sangat Kurang' , 'Sangat Kurang'),
        )
    
    TB_U = (
            ('Normal' , 'Normal'),
            ('Pendek' , 'Pendek'),
            ('Tinggi' , 'Tinggi'),
            ('Sangat Pendek' , 'Sangat Pendek'),
        )
    
    BB_TB = (
            ('Gizi Kurang' , 'Gizi Kurang'),
            ('Gizi Baik' , 'Gizi Baik'),
        )
    
    PTS = (
            ('Potensi Stunting' , 'Potensi Stunting'),
            ('Stunting' , 'Stunting'),
            ('Tidak' , 'Tidak'),
        )
    
    nama           = models.CharField(max_length=100)
    jk             = models.CharField(max_length=100, choices=JK)
    tangga_lahir   = models.CharField(max_length=100)
    desa           = models.CharField(max_length=100)
    posyandu       = models.CharField(max_length=100)
    alamat         = models.CharField(max_length=100)
    status_KM      = models.CharField(max_length=100,choices=STKM)
    usia_ukur      = models.IntegerField()
    bb             = models.IntegerField()
    tb             = models.IntegerField()
    bb_u           = models.CharField(max_length=100,choices=BB_U)
    tb_u           = models.CharField(max_length=100,choices=TB_U)
    bb_tb          = models.CharField(max_length=100,choices=BB_TB)
    stunting       = models.CharField(max_length=100,choices=PTS)
    
    def __str__(self) :
        return self.nama 
    
    # ===================== MEMBUAT DATABASE KEECAMATAN BR 1 ================
class Kecamatan_br2(models.Model):
    JK = (
            ('L' , 'L'),
            ('P' , 'P'),
        )
    
    STKM = (
            ('Kurang Mampu' , 'Kurang Mampu'),
            ('Tidak' , 'Tidak'),
        )
    
    BB_U = (
            ('Berat Badan Normal' , 'Berat Badan Normal'),
            ('Kurang' , 'Kurang'),
            ('Risiko Lebih' , 'Risiko Lebih'),
            ('Sangat Kurang' , 'Sangat Kurang'),
        )
    
    TB_U = (
            ('Normal' , 'Normal'),
            ('Pendek' , 'Pendek'),
            ('Tinggi' , 'Tinggi'),
            ('Sangat Pendek' , 'Sangat Pendek'),
        )
    
    BB_TB = (
            ('Gizi Kurang' , 'Gizi Kurang'),
            ('Gizi Baik' , 'Gizi Baik'),
        )
    
    PTS = (
            ('Potensi Stunting' , 'Potensi Stunting'),
            ('Stunting' , 'Stunting'),
            ('Tidak' , 'Tidak'),
        )
    
    nama           = models.CharField(max_length=100)
    jk             = models.CharField(max_length=100, choices=JK)
    tangga_lahir   = models.CharField(max_length=100)
    desa           = models.CharField(max_length=100)
    posyandu       = models.CharField(max_length=100)
    alamat         = models.CharField(max_length=100)
    status_KM      = models.CharField(max_length=100,choices=STKM)
    usia_ukur      = models.FloatField()
    bb             = models.FloatField()
    tb             = models.FloatField()
    bb_u           = models.CharField(max_length=100,choices=BB_U)
    tb_u           = models.CharField(max_length=100,choices=TB_U)
    bb_tb          = models.CharField(max_length=100,choices=BB_TB)
    stunting       = models.CharField(max_length=100,choices=PTS)
    
    def __str__(self) :
        return self.nama 

    # ===================== MEMBUAT DATABASE DATA TRAINING ================
class Data_Training(models.Model):
    JK = (
            ('L' , 'L'),
            ('P' , 'P'),
        )
    
    STKM = (
            ('Kurang Mampu' , 'Kurang Mampu'),
            ('Tidak' , 'Tidak'),
        )
    
    BB_U = (
            ('Berat Badan Normal' , 'Berat Badan Normal'),
            ('Kurang' , 'Kurang'),
            ('Sangat Kurang' , 'Sangat Kurang'),
        )
    
    TB_U = (
            ('Normal' , 'Normal'),
            ('Pendek' , 'Pendek'),
            ('Tinggi' , 'Tinggi'),
            ('Sangat Pendek' , 'Sangat Pendek'),
        )
    
    BB_TB = (
            ('Gizi Kurang' , 'Gizi Kurang'),
            ('Gizi Baik' , 'Gizi Baik'),
        )
    
    PTS = (
            ('Potensi Stunting' , 'Potensi Stunting'),
            ('Stunting' , 'Stunting'),
            ('Tidak' , 'Tidak'),
        )
    
    jk             = models.CharField(max_length=100, choices=JK)
    status_KM      = models.CharField(max_length=100,choices=STKM)
    usia_ukur      = models.FloatField()
    bb_u           = models.CharField(max_length=100,choices=BB_U)
    tb_u           = models.CharField(max_length=100,choices=TB_U)
    bb_tb          = models.CharField(max_length=100,choices=BB_TB)
    stunting       = models.CharField(max_length=100,choices=PTS)
    
    def __str__(self) :
        return self.nama 
    

    # ===================== MEMBUAT DATABASE DATA Testing ================
class Data_Testing(models.Model):
    JK = (
            ('L' , 'L'),
            ('P' , 'P'),
        )
    
    STKM = (
            ('Kurang Mampu' , 'Kurang Mampu'),
            ('Tidak' , 'Tidak'),
        )
    
    BB_U = (
            ('Berat Badan Normal' , 'Berat Badan Normal'),
            ('Kurang' , 'Kurang'),
            ('Sangat Kurang' , 'Sangat Kurang'),
        )
    
    TB_U = (
            ('Normal' , 'Normal'),
            ('Pendek' , 'Pendek'),
            ('Tinggi' , 'Tinggi'),
            ('Sangat Pendek' , 'Sangat Pendek'),
        )
    
    BB_TB = (
            ('Gizi Kurang' , 'Gizi Kurang'),
            ('Gizi Baik' , 'Gizi Baik'),
        )
    
    PTS = (
            ('Potensi Stunting' , 'Potensi Stunting'),
            ('Stunting' , 'Stunting'),
            ('Tidak' , 'Tidak'),
        )
    
    jk             = models.CharField(max_length=100, choices=JK)
    status_KM      = models.CharField(max_length=100,choices=STKM)
    usia_ukur      = models.FloatField()
    bb_u           = models.CharField(max_length=100,choices=BB_U)
    tb_u           = models.CharField(max_length=100,choices=TB_U)
    bb_tb          = models.CharField(max_length=100,choices=BB_TB)
    stunting       = models.CharField(max_length=100,choices=PTS)
    
    def __str__(self) :
        return self.nama 

# Membuat Model Agenda
class Agenda(models.Model):
    kegiatan = models.CharField(max_length=100)
    def __str__(self) :
        return self.nama 
    
# Membuat Model Agenda Baru
class AgendaBaru(models.Model):
    kegiatan = models.CharField(max_length=100)
    hari = models.CharField(max_length=100)
    def __str__(self) :
        return self.kegiatan 

# Membuat Model hasil Prediksi
class Data_Prediksi(models.Model):
    JK = (
            ( 1 , 'L'),
            ( 0 , 'P'),
        )
    
    STKM = (
            ( 1 , 'Kurang Mampu'),
            ( 0 , 'Mampu'),
        )
    
    Usia_ukur = (
            (1 , 'Lebih Dari 3 Tahun'),
            (0 , '3 Tahun'),
            (2, 'Kurang Dari 3 Tahun'),
        )

    BB_U = (
            (1 , 'BB Normal'),
            (0 , 'BB Kurang'),
            (2 , 'BB Sangat Kurang'),
        )
    
    TB_U = (
            (3 , 'TB Tinggi'),
            (1 , 'TB Normal'),
            (0 , 'TB Pendek'),
            (2 , 'TB Sangat Pendek'),
        )
    
    BB_TB = (
            ( 0 , 'Gizi Kurang'),
            ( 1 , 'Gizi Baik'),
        )
    nama           = models.CharField(max_length=100)
    jk             = models.PositiveIntegerField(choices=JK)
    status_KM      = models.PositiveIntegerField(choices=STKM)
    usia_ukur      = models.PositiveIntegerField(choices=Usia_ukur)
    bb_u           = models.PositiveIntegerField(choices=BB_U)
    tb_u           = models.PositiveIntegerField(choices=TB_U)
    bb_tb          = models.PositiveIntegerField(choices=BB_TB)
    predictions    = models.CharField(max_length=100, blank=True)
    date           = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        model = load('./savedModels/model_apps_stunted.joblib')
        self.predictions = model.predict(
            [[self.jk, self.status_KM, self.usia_ukur, self.bb_u, self.tb_u, self.bb_tb]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.nama