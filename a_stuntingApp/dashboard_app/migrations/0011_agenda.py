# Generated by Django 4.1.7 on 2023-04-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0010_alter_data_prediksi_bb_tb_alter_data_prediksi_bb_u_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kegiatan', models.CharField(max_length=100)),
            ],
        ),
    ]
