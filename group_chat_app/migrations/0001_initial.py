# Generated by Django 4.0.6 on 2022-08-02 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.TextField(blank=True, null=True)),
                ('user_name', models.CharField(max_length=128)),
                ('group_name', models.CharField(max_length=128)),
                ('likes', models.BigIntegerField(blank=True, null=True)),
                ('dislikes', models.BigIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
