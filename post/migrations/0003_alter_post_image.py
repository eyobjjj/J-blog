# Generated by Django 4.2.13 on 2024-09-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_author_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
