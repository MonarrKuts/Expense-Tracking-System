# Generated by Django 4.2.7 on 2024-02-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_remove_expense_category_remove_expense_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='id',
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]