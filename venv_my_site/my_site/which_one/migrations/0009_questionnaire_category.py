# Generated by Django 3.2 on 2021-04-28 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('which_one', '0008_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='which_one.category', verbose_name='カテゴリー'),
            preserve_default=False,
        ),
    ]
