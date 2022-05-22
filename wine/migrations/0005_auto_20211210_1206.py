# Generated by Django 3.2.9 on 2021-12-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0004_auto_20211209_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denominationwine',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='denominationwine',
            name='order',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='aromas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='berry_pruning',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='clones',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='colour',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='comment_grape',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='creator',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='cultural_aptures',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='description_tastes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='description_visual',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='disease_sensitivity',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='maturity',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='phenology',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='potential_garde',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='skins',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='species',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='survey_hectares',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='technical_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='type_variety',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='year_cross',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grape',
            name='yields',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grapeassembly',
            name='main_accessory',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grapeassembly',
            name='percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grapemainaccessory',
            name='main_accessory',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grapeprofile',
            name='acidity_taste',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grapeprofile',
            name='alcohol_taste',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grapeprofile',
            name='aroma_complexity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grapeprofile',
            name='aroma_intensity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grapeprofile',
            name='aroma_length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grapeprofile',
            name='body_taste',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grapeprofile',
            name='general_note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sugardose',
            name='max_sugar_concentration',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sugardose',
            name='min_sugar_concentration',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sugardose',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sugardose',
            name='type_wine',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='winecdc',
            name='colour',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='winecdc',
            name='comment_descritpion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='winecdc',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='winecdc',
            name='type',
            field=models.TextField(blank=True, null=True),
        ),
    ]