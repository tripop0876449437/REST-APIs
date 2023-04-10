# Generated by Django 4.1.7 on 2023-04-10 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_reward'),
    ]

    operations = [
        migrations.CreateModel(
            name='RewardHistory',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('point_used', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updatated_at', models.DateTimeField(auto_now=True)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
                ('reward_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.reward')),
            ],
        ),
    ]
