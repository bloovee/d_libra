# Generated by Django 4.0.3 on 2022-06-18 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0028_parentcategory_created_at_parentcategory_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapi.parentcategory'),
        ),
    ]
