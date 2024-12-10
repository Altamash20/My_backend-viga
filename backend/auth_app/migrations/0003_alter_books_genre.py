# Generated by Django 4.0.10 on 2024-12-09 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_books_review_delete_book_management'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='Genre',
            field=models.CharField(choices=[('LR', 'Literary'), ('HS', 'History'), ('HR', 'Horror'), ('FN', 'Fiction'), ('SCN', 'Science'), ('OTH', 'Other')], max_length=100),
        ),
    ]