# Generated by Django 2.1.7 on 2019-03-06 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_courses', '0004_auto_20190306_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses', to='student_courses.Student'),
        ),
    ]