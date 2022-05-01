# Generated by Django 2.2.6 on 2019-10-12 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('mobile', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'ContactUs',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=6)),
                ('bod', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='images/User/')),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('shopname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='images/Supplier/')),
            ],
            options={
                'db_table': 'Supplier',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=20)),
                ('prod_photo', models.ImageField(upload_to='images/product/')),
                ('prod_price', models.IntegerField()),
                ('prod_description', models.TextField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medical_Management.Category')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]