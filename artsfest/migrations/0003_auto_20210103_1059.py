# Generated by Django 3.1.4 on 2021-01-03 10:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('artsfest', '0002_remove_events_event_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='group_Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('team_mem1', models.CharField(max_length=200)),
                ('team_mem2', models.CharField(max_length=200)),
                ('team_mem3', models.CharField(max_length=200)),
                ('team_mem4', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='individual_Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=20)),
                ('team_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='event_sic',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='event_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Participants',
        ),
        migrations.AddField(
            model_name='individual_participants',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artsfest.events'),
        ),
        migrations.AddField(
            model_name='group_participants',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artsfest.events'),
        ),
    ]