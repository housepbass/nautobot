# Generated by Django 3.2.18 on 2023-05-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("extras", "0085_taggeditem_cleanup"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taggeditem",
            name="object_id",
            field=models.UUIDField(db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name="taggeditem",
            unique_together={("content_type", "object_id", "tag")},
        ),
    ]
