# Generated by Django 2.2.12 on 2023-08-01 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='items_images')),
                ('is_sold', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='items.Category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
