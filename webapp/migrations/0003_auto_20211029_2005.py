# Generated by Django 3.2.8 on 2021-10-29 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_contact_event_group_grouprole_role_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField()),
                ('date_expired', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.member')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.role')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMembershipRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField()),
                ('date_expired', models.DateField()),
                ('remarks', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('group_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.grouprole')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('date_exited', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.group')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='GroupEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.event')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.group')),
            ],
        ),
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.branch')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='branches',
            field=models.ManyToManyField(through='webapp.EventLocation', to='webapp.Branch'),
        ),
        migrations.AddField(
            model_name='event',
            name='groups',
            field=models.ManyToManyField(through='webapp.GroupEvent', to='webapp.Group'),
        ),
        migrations.AddField(
            model_name='member',
            name='group_roles',
            field=models.ManyToManyField(through='webapp.GroupMembershipRole', to='webapp.GroupRole'),
        ),
        migrations.AddField(
            model_name='member',
            name='groups',
            field=models.ManyToManyField(through='webapp.GroupMembership', to='webapp.Group'),
        ),
        migrations.AddField(
            model_name='member',
            name='roles',
            field=models.ManyToManyField(through='webapp.MemberRole', to='webapp.Role'),
        ),
    ]
