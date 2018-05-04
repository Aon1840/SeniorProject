# Generated by Django 2.0.3 on 2018-05-04 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0002_auto_20180503_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarPosition',
            fields=[
                ('carPosition_id', models.AutoField(primary_key=True, serialize=False)),
                ('position_id', models.CharField(max_length=3)),
                ('is_driveOut', models.BooleanField(default=False)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.User')),
            ],
            options={
                'ordering': ('carPosition_id',),
            },
        ),
    ]
