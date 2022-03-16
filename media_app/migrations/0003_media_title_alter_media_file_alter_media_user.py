# Generated by Django 4.0.3 on 2022-03-12 19:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import media_app.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media_app', '0002_alter_media_file_alter_media_file_webp'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='title',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(('png', 'jpg', 'jpeg'), message='File of this format cannot be load'), media_app.validators.MaxSizeValidator(5)]),
        ),
        migrations.AlterField(
            model_name='media',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL),
        ),
    ]