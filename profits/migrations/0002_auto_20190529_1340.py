# Generated by Django 2.2.1 on 2019-05-29 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profitmachine',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='branches.Branch', verbose_name='สาขา'),
        ),
    ]