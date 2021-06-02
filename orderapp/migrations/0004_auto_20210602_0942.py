# Generated by Django 2.2.23 on 2021-06-02 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0003_auto_20210602_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='orderapp.Cart'),
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderapp.Customer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orderapp.Products'),
        ),
    ]
