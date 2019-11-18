# Generated by Django 2.2.6 on 2019-11-18 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20191118_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='college',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('IT', 'Information Technologies'), ('Bussiness Managment', 'Bussiness Managment'), ('Digital Marketing', 'Digital Marketing'), ('Computer Science', 'Computer Science'), ('Civil Engineering', 'Civil Engineering'), ('AI', 'Artificial & Inteligence'), ('Other', 'Other')], default=1, max_length=120),
        ),
        migrations.AddField(
            model_name='education',
            name='ended_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='is_currently_studying',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='education',
            name='started_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='ended_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='is_currently_working',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='profession',
            field=models.CharField(choices=[('Student or Learning', 'Student or Learning'), ('Junior Developer', 'Junior Developer'), ('Senior Developer', 'Senior Developer'), ('Developer', 'Developer'), ('Manager', 'Manager'), ('Instructor or Teacher', 'Instructor or Teacher'), ('Intern', 'Intern'), ('ussiness Man', 'Bussiness Man'), ('Digital Marketer', 'Digital Marketer'), ('Data Scientist', 'Data Scientist'), ('Other', 'Other')], default=1, max_length=120),
        ),
        migrations.AddField(
            model_name='experience',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='experience',
            name='started_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]