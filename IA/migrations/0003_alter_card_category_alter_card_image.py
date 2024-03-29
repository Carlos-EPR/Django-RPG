# Generated by Django 5.0.1 on 2024-01-31 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IA', '0002_card_image_card_serial_card_user_alter_card_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='category',
            field=models.CharField(choices=[('Weapons', 'Option1'), ('Potions', 'Option2'), ('Armors', 'Option3')], default='Weapons', max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.BinaryField(),
        ),
    ]
