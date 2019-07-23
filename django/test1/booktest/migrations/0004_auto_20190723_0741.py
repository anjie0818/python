# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20190723_0717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='idDelete',
            new_name='isDelete',
        ),
        migrations.RenameField(
            model_name='heroinfo',
            old_name='idDelete',
            new_name='isDelete',
        ),
    ]
