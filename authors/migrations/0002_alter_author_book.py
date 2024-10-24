# Generated by Django 5.1.2 on 2024-10-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(related_name='written_books', to='books.book'),
        ),
    ]
