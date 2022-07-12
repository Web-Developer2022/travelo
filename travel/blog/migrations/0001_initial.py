# Generated by Django 4.0.5 on 2022-07-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, verbose_name='Yonalish nomi*')),
                ('text', models.TextField(blank=True, default='text yoq', max_length=2500, verbose_name='Yonalish haqida*')),
                ('image', models.ImageField(upload_to='images', verbose_name='Rasm*')),
                ('price', models.PositiveIntegerField(default=100, verbose_name='Yonalish narxi*')),
                ('price_usd', models.PositiveIntegerField(default=100, verbose_name='Yonalish narxi*')),
                ('leave', models.DateField(blank=True, verbose_name='Ketish sanasi ')),
                ('back_to', models.DateField(blank=True, verbose_name='Qaytish sannasi')),
            ],
            options={
                'verbose_name': 'Yonalish',
                'verbose_name_plural': 'Yonalishlar',
            },
        ),
    ]
