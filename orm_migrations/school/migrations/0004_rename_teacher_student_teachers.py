# Generated by Django 4.2.2 on 2023-06-26 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
