# Generated by Django 4.2.5 on 2023-10-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_link_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='url',
            field=models.URLField(default='test', help_text='Enter a link of a website', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(help_text='Enter the name of a website', max_length=100),
        ),
    ]
