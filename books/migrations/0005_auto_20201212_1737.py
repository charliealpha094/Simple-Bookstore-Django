# Generated by Django 3.1.4 on 2020-12-12 17:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20201210_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['id'], name='id_index'),
        ),
    ]
