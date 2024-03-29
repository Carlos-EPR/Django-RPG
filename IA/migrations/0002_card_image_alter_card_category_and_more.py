# Generated by Django 5.0.1 on 2024-01-26 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.CharField(default='default.png', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='category',
            field=models.CharField(choices=[('Weapon', 'Option1'), ('Potion', 'Option2'), ('Armor', 'Option3')], default='Weapons', max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
