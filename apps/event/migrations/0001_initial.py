# Generated by Django 3.2.3 on 2021-05-24 18:54

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('description', django_quill.fields.QuillField(verbose_name='add description')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(default='2021-12-12')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='event-images/')),
                ('max_enroll', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.student')),
            ],
        ),
    ]