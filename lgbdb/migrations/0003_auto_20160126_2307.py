# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgbdb', '0002_benchmark_fps_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='benchmark',
            name='desktop_environment',
        ),
        migrations.RemoveField(
            model_name='benchmark',
            name='kernel',
        ),
        migrations.RemoveField(
            model_name='benchmark',
            name='linux_distribution',
        ),
        migrations.RemoveField(
            model_name='benchmark',
            name='window_manager',
        ),
        migrations.RemoveField(
            model_name='system',
            name='desktop_environment',
        ),
        migrations.RemoveField(
            model_name='system',
            name='kernel',
        ),
        migrations.RemoveField(
            model_name='system',
            name='linux_distribution',
        ),
        migrations.RemoveField(
            model_name='system',
            name='window_manager',
        ),
        migrations.AddField(
            model_name='benchmark',
            name='operative_system',
            field=models.CharField(blank=True, choices=[(b'Opensource', b'Opensource'), (b'Proprietary', b'Proprietary')], max_length=50),
        ),
        migrations.AddField(
            model_name='system',
            name='operative_system',
            field=models.CharField(choices=[('Windows', (('Windows XP', 'Windows XP'), ('Windows Vista', 'Windows Vista'), ('Windows 7', 'Windows 7'), ('Windows 8', 'Windows 8'), ('Windows 10', 'Windows 10'), ('Windows-other', 'Windows-other'))), ('Linux', (('Debian-based (Debian, Ubuntu, Mint, Elementary OS, SteamOS)', 'Debian-based (Debian, Ubuntu, Mint, Elementary OS, SteamOS)'), ('Arch-based (Arch, Manjaro)', 'Arch-based (Arch, Manjaro)'), ('Red Hat-based (RedHat, Fedora, CentOS)', 'Red Hat-based (RedHat, Fedora, CentOS)'), ('Gentoo-based (Gentoo, Chromium, Funtoo)', 'Gentoo-based (Gentoo, Chromium, Funtoo)'), ('SUSE-based', 'SUSE-based'), ('Slackware-based', 'Slackware-based'), ('Mandriva-based', 'Mandriva-based'), ('Linux-other', 'Linux-other')))], default='Linux-other', max_length=80),
        ),
    ]
