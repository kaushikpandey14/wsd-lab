# Generated by Django 3.1.3 on 2020-11-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='general_safety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('General_Safety_Items', models.CharField(default=' ', max_length=900, null=True)),
                ('radio', models.CharField(default=' ', max_length=300, null=True)),
                ('Explanation_of_the_deviation', models.CharField(default=' ', max_length=400, null=True)),
                ('Action_Item_description', models.CharField(default=' ', max_length=400, null=True)),
                ('Responsibility', models.CharField(default=' ', max_length=300, null=True)),
                ('Plan_date_of_completion', models.CharField(default=' ', max_length=15, null=True)),
                ('Actual_date_of_completion', models.CharField(default=' ', max_length=15, null=True)),
                ('Sever', models.CharField(default=' ', max_length=300, null=True)),
            ],
        ),
    ]
