# Generated by Django 5.1.2 on 2024-11-05 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0001_initial'),
        ('users', '0005_remove_customuser_booklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='booklist',
            field=models.ManyToManyField(blank=True, related_name='lists', to='booklist.booklist'),
        ),
    ]