from django.db import migrations, models, connection

def remove_existing_constraint(apps, schema_editor):
    with connection.cursor() as cursor:
        # Verificar si existe una restricción única en la columna 'EMAIL'
        cursor.execute("""
            SELECT uc.constraint_name
            FROM user_cons_columns ucc
            JOIN user_constraints uc ON uc.constraint_name = ucc.constraint_name
            WHERE ucc.column_name = 'EMAIL' AND uc.table_name = 'SIVARIA_APPUSER' AND uc.constraint_type = 'U'
        """)
        result = cursor.fetchone()

        if result:
            # Si existe una restricción única, la eliminamos
            constraint_name = result[0]
            schema_editor.execute(f"""
                ALTER TABLE "SIVARIA_APPUSER" 
                DROP CONSTRAINT "{constraint_name}"
            """)

class Migration(migrations.Migration):

    dependencies = [
        ("sivaria", "0005_alter_pushnotificationtype_data"),
    ]

    operations = [
        # Primero, eliminamos la restricción existente si la hay
        migrations.RunPython(remove_existing_constraint, atomic=False),
        # Luego, aplicamos las nuevas opciones de modelo
        migrations.AlterModelOptions(
            name="appuser",
            options={},
        ),
        migrations.AlterUniqueTogether(
            name="appuser",
            unique_together={("email",)},
        ),
    ]
