# Generated by Django 3.1.2 on 2021-03-02 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_auto_20201201_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.book'),
        ),
    ]
