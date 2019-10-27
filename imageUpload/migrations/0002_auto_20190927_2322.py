# Generated by Django 2.2.4 on 2019-09-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageUpload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='paperModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='questionpaper')),
                ('course_code', models.CharField(max_length=5)),
                ('year', models.IntegerField()),
                ('tierce', models.IntegerField()),
                ('instructor', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='imageModel',
        ),
    ]
