from django.db import migrations, models
import datetime   
class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default=datetime.date.today),  # ✅ valid default
            preserve_default=False,
        ),
    ]
