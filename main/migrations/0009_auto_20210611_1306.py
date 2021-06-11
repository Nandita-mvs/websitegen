# Generated by Django 3.1.2 on 2021-06-11 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210611_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='behancelink',
            field=models.CharField(blank=True, default='', max_length=2000, verbose_name='Behance URL'),
        ),
        migrations.AlterField(
            model_name='member',
            name='githublink',
            field=models.CharField(blank=True, default='', max_length=2000, verbose_name='Github URL'),
        ),
        migrations.AlterField(
            model_name='member',
            name='instagramlink',
            field=models.CharField(blank=True, default='', max_length=2000, verbose_name='Instagram URL'),
        ),
        migrations.AlterField(
            model_name='member',
            name='linkedinlink',
            field=models.CharField(blank=True, default='', max_length=2000, verbose_name='Linkedin URL'),
        ),
        migrations.AlterField(
            model_name='member',
            name='project4',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Project 4 name'),
        ),
        migrations.AlterField(
            model_name='member',
            name='project5',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Project 5 name'),
        ),
        migrations.AlterField(
            model_name='member',
            name='project6',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Project 6 name'),
        ),
        migrations.AlterField(
            model_name='member',
            name='resume',
            field=models.CharField(blank=True, default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='member',
            name='twitterlink',
            field=models.CharField(blank=True, default='', max_length=2000, verbose_name='Twitter URL'),
        ),
        migrations.AlterField(
            model_name='member',
            name='work4',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Project 4 URL'),
        ),
        migrations.AlterField(
            model_name='member',
            name='work5',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Project 5 URL'),
        ),
        migrations.AlterField(
            model_name='member',
            name='work6',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Project 6 URL'),
        ),
    ]
