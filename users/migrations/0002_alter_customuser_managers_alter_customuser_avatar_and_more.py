# Generated by Django 4.0 on 2022-01-29 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='media', upload_to='avatars/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_followed', to='users.customuser')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_following', to='users.customuser')),
            ],
            options={
                'verbose_name': 'Following user',
                'verbose_name_plural': 'Following users',
            },
        ),
        migrations.AddConstraint(
            model_name='userfollow',
            constraint=models.UniqueConstraint(fields=('follower', 'followed'), name='unique_following'),
        ),
    ]