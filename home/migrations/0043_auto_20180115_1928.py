# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-15 19:28
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_participation_intern_funding_sources'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggedSponsorChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.DateField(auto_now_add=True, verbose_name='Date coordinator made sponsorship change')),
                ('interns_funded', models.IntegerField(verbose_name='New intern amount')),
                ('intern_funding_sources', ckeditor.fields.RichTextField(help_text='New funding sources text')),
                ('modifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Comrade')),
            ],
        ),
        migrations.AlterField(
            model_name='participation',
            name='intern_funding_sources',
            field=ckeditor.fields.RichTextField(default='', help_text='<p>For each source of funding for interns:<ol><li>What is the sponsor name?</li><li>What is the sponsorship dollar amount?</li><li>Is the funding is secured or tentative?</li><li>If the funding is tentative, please provide a date by which you will have a decision on your funding. Funding must be secured by intern selection time for this round.</li><li>Any additional information you need Outreachy organizers to know about this sponsorship.</li></ol><p>Outreachy organizers will be in touch with coordinators later to gather invoicing information.</p>'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='interns_funded',
            field=models.IntegerField(default=0, verbose_name='How many interns do you expect to fund for this round?'),
        ),
        migrations.AddField(
            model_name='loggedsponsorchange',
            name='participation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Participation'),
        ),
    ]