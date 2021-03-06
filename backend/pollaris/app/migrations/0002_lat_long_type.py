# Generated by Django 2.2.6 on 2019-12-04 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="dropboxlocation",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=9, max_digits=38, null=True
            ),
        ),
        migrations.AlterField(
            model_name="dropboxlocation",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=9, max_digits=38, null=True
            ),
        ),
        migrations.AlterField(
            model_name="earlyvotelocation",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=9, max_digits=38, null=True
            ),
        ),
        migrations.AlterField(
            model_name="earlyvotelocation",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=9, max_digits=38, null=True
            ),
        ),
        migrations.AlterField(
            model_name="pollinglocation",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=9, max_digits=38, null=True
            ),
        ),
        migrations.AlterField(
            model_name="pollinglocation",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=9, max_digits=38, null=True
            ),
        ),
    ]
