# Generated by Django 3.2 on 2021-05-04 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('which_one', '0020_auto_20210430_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='votes_A',
            new_name='vote_A',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='votes_B',
            new_name='vote_B',
        ),
        migrations.AlterField(
            model_name='choice',
            name='ip_address',
            field=models.CharField(default=0, max_length=50, verbose_name='IPアドレス'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='user',
            field=models.ForeignKey(default='名無し', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
    ]
