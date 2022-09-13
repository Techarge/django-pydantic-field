# Generated by Django 4.0.6 on 2022-09-05 09:02

from django.db import migrations, models
import django_pydantic_field.fields
import tests.sample_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name="Building",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("meta", django_pydantic_field.fields.PydanticSchemaField(config=None, default={"type": "frame"}, schema="BuildingMeta")),
                ("meta_builtin_list", django_pydantic_field.fields.PydanticSchemaField(config=None, default=list, schema=django_pydantic_field.fields.GenericContainer(list, (tests.sample_app.models.BuildingMeta,)))),
                ("meta_typing_list", django_pydantic_field.fields.PydanticSchemaField(config=None, default=list, schema=django_pydantic_field.fields.GenericContainer(list, (tests.sample_app.models.BuildingMeta,)))),
                ("meta_untyped_list", django_pydantic_field.fields.PydanticSchemaField(config=None, default=list, schema=list)),
                ("meta_untyped_builtin_list", django_pydantic_field.fields.PydanticSchemaField(config=None, default=list, schema=list)),
            ],
        ),

        migrations.CreateModel(
            name="PostponedBuilding",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("meta", django_pydantic_field.fields.PydanticSchemaField(config=None, default={"type": "frame"}, schema="BuildingMeta")),
                ("meta_builtin_list", django_pydantic_field.fields.PydanticSchemaField(config=None, default=list, schema=django_pydantic_field.fields.GenericContainer(list, (tests.sample_app.models.BuildingMeta,)))),
                ("meta_typing_list", django_pydantic_field.fields.PydanticSchemaField(config=None, default=list, schema=django_pydantic_field.fields.GenericContainer(list, (tests.sample_app.models.BuildingMeta,)))),
                ("meta_untyped_list", django_pydantic_field.fields.PydanticSchemaField(config=None, default=list, schema=list)),
                ("meta_untyped_builtin_list", django_pydantic_field.fields.PydanticSchemaField(config=None, default=list, schema=list)),
            ],
        ),
    ]
