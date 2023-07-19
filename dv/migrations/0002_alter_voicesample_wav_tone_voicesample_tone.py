# Generated by Django 4.2.3 on 2023-07-19 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import dv.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voicesample',
            name='wav',
            field=models.FileField(upload_to=dv.utils.voice_samples_directory_path),
        ),
        migrations.CreateModel(
            name='Tone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weights', models.FileField(upload_to=dv.utils.tones_directory_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='voicesample',
            name='tone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dv.tone'),
        ),
    ]
