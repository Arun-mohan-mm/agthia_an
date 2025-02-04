# Generated by Django 5.0.8 on 2024-08-12 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agthi', '0012_restaurants_social_media_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurants',
            old_name='social_media_link',
            new_name='facebook_link',
        ),
        migrations.AddField(
            model_name='restaurants',
            name='instagram_link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='twitter_link',
            field=models.URLField(null=True),
        ),
    ]
