# Generated by Django 3.2.7 on 2022-06-26 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr_portal', '0008_alter_userprofile_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cr_id',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='college',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='points',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sop',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='whatsapp',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year',
            field=models.CharField(default='', max_length=200),
        ),
    ]