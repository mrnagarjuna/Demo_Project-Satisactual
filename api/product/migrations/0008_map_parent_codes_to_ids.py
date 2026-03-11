from django.db import migrations

def map_parent(apps, schema_editor):
    MstProdCodes = apps.get_model("product", "MstProdCodes")

    for row in MstProdCodes.objects.exclude(cod_parent_product__isnull=True):
        parent_code = row.cod_parent_product

        try:
            parent = MstProdCodes.objects.get(cod_product=parent_code)
            row.cod_parent_product = parent.id
            row.save(update_fields=["cod_parent_product"])
        except MstProdCodes.DoesNotExist:
            row.cod_parent_product = None
            row.save(update_fields=["cod_parent_product"])

class Migration(migrations.Migration):

    dependencies = [
    ("product", "0007_alter_mstprodcodes_cod_parent_product_and_more"),
]


    operations = [
        migrations.RunPython(map_parent)
    ]
