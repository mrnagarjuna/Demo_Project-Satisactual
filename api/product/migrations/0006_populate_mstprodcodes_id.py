from django.db import migrations

def populate_ids(apps, schema_editor):
    MstProdCodes = apps.get_model('product', 'MstProdCodes')
    counter = 1
    for obj in MstProdCodes.objects.all():
        if obj.id is None:
            obj.id = counter
            obj.save(update_fields=['id'])
            counter += 1

class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_mstprodcodes_id'),
    ]

    operations = [
        migrations.RunPython(populate_ids),
    ]
