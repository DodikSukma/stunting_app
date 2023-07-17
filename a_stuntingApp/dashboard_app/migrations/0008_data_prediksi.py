# Generated by Django 4.1.7 on 2023-04-14 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0007_data_testing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Prediksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('jk', models.CharField(choices=[(1, 'L'), (0, 'P')], max_length=100)),
                ('status_KM', models.CharField(choices=[(1, 'Kurang Mampu'), (0, 'Mampu')], max_length=100)),
                ('usia_ukur', models.CharField(choices=[(1, 'Lebih Dari 3 Tahun'), (0, '3 Tahun'), (2, 'Kurang Dari 3 Tahun')], max_length=100)),
                ('bb_u', models.CharField(choices=[(1, 'BB Normal'), (0, 'BB Kurang'), (2, 'BB Sangat Kurang')], max_length=100)),
                ('tb_u', models.CharField(choices=[(3, 'TB Tinggi'), (1, 'TB Normal'), (0, 'TB Pendek'), (2, 'TB Sangat Pendek')], max_length=100)),
                ('bb_tb', models.CharField(choices=[(0, 'Gizi Kurang'), (1, 'Gizi Baik')], max_length=100)),
                ('predictions', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]