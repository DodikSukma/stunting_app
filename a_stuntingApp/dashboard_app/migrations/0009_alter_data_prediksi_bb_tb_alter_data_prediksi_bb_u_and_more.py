# Generated by Django 4.1.7 on 2023-04-14 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0008_data_prediksi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_prediksi',
            name='bb_tb',
            field=models.PositiveIntegerField(choices=[(0, 'Gizi Kurang'), (1, 'Gizi Baik')], max_length=100),
        ),
        migrations.AlterField(
            model_name='data_prediksi',
            name='bb_u',
            field=models.PositiveIntegerField(choices=[(1, 'BB Normal'), (0, 'BB Kurang'), (2, 'BB Sangat Kurang')], max_length=100),
        ),
        migrations.AlterField(
            model_name='data_prediksi',
            name='jk',
            field=models.PositiveIntegerField(choices=[(1, 'L'), (0, 'P')], max_length=100),
        ),
        migrations.AlterField(
            model_name='data_prediksi',
            name='status_KM',
            field=models.PositiveIntegerField(choices=[(1, 'Kurang Mampu'), (0, 'Mampu')], max_length=100),
        ),
        migrations.AlterField(
            model_name='data_prediksi',
            name='tb_u',
            field=models.PositiveIntegerField(choices=[(3, 'TB Tinggi'), (1, 'TB Normal'), (0, 'TB Pendek'), (2, 'TB Sangat Pendek')], max_length=100),
        ),
        migrations.AlterField(
            model_name='data_prediksi',
            name='usia_ukur',
            field=models.PositiveIntegerField(choices=[(1, 'Lebih Dari 3 Tahun'), (0, '3 Tahun'), (2, 'Kurang Dari 3 Tahun')], max_length=100),
        ),
    ]