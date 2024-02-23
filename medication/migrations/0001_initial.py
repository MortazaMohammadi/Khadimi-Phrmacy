# Generated by Django 5.0.2 on 2024-02-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_code', models.CharField(max_length=200)),
                ('medication_name', models.CharField(max_length=200)),
                ('medication_cost', models.FloatField()),
                ('note', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]