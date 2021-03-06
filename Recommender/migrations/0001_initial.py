# Generated by Django 3.1.5 on 2021-01-27 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('recommend_id', models.IntegerField(primary_key=True, serialize=False)),
                ('moviesToReturn', models.ManyToManyField(to='movies.Movies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
