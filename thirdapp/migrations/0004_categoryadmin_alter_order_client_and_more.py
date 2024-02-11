# Generated by Django 5.0.1 on 2024-02-08 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0003_alter_order_client_remove_order_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(db_column='client', on_delete=django.db.models.deletion.CASCADE, to='thirdapp.client', to_field='name'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.CreateModel(
            name='ProductAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thirdapp.categoryadmin')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(db_column='product', default=1, on_delete=django.db.models.deletion.CASCADE, to='thirdapp.product', to_field='name'),
            preserve_default=False,
        ),
    ]