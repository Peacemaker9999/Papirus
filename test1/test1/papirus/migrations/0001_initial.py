# Generated by Django 4.1.1 on 2022-09-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Papirus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('where', models.CharField(max_length=40)),
                ('initiator', models.CharField(max_length=40)),
                ('type_documents', models.CharField(max_length=40)),
                ('registr_number', models.CharField(max_length=20)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('complate_status', models.CharField(max_length=40)),
            ],
        ),
    ]
