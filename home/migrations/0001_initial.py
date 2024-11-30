# Generated by Django 5.1.3 on 2024-11-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resumeHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('dob', models.DateField()),
                ('state', models.CharField(choices=[('India', 'India'), ('Nepal', 'Nepal'), ('America', 'America')], max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='image')),
                ('rdoc', models.FileField(upload_to='rdoc')),
            ],
        ),
    ]