# Generated by Django 5.0.6 on 2024-08-05 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blogs_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
    ]
