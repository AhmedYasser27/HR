from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ems_admin', '0002_auto_20200712_1620'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EMSPermission',
        ),
    ]
