# Generated by Django 5.0.1 on 2024-02-08 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0004_categoryadmin_alter_order_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productadmin',
            name='category',
        ),
        migrations.DeleteModel(
            name='CategoryAdmin',
        ),
        migrations.DeleteModel(
            name='ProductAdmin',
        ),
    ]