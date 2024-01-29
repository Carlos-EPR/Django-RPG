# Generated by Django 5.0.1 on 2024-01-26 20:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Weapon', 'Option1'), ('Potion', 'Option2'), ('Armor', 'Option3')], max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('rarity', models.CharField(choices=[('Bronze', 'Option1'), ('Silver', 'Option2'), ('Gold', 'Option3'), ('Emerald', 'Option4'), ('Diamond', 'Option5'), ('Ruby', 'Option6'), ('Obsidian', 'Option7'), ('Opal', 'Option8')], max_length=20)),
                ('type', models.CharField(choices=[('Sword', 'Option1'), ('Axe', 'Option2'), ('Crossbow', 'Option3'), ('Spear', 'Option4'), ('Dagger', 'Option5'), ('Wand', 'Option6')], max_length=20)),
                ('status_card', models.IntegerField()),
                ('power', models.IntegerField()),
                ('description', models.CharField(max_length=150)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rarity', models.CharField(choices=[('Bronze', 'Option1'), ('Silver', 'Option2'), ('Gold', 'Option3'), ('Emerald', 'Option4'), ('Diamond', 'Option5'), ('Ruby', 'Option6'), ('Obsidian', 'Option7'), ('Opal', 'Option8')], max_length=20)),
                ('attribute', models.CharField(choices=[('STR', 'Option1'), ('VIT', 'Option2'), ('RES', 'Option3'), ('AGI', 'Option4'), ('LUC', 'Option5'), ('INT', 'Option6')], max_length=10)),
                ('stats', models.IntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IA.card')),
            ],
        ),
    ]
