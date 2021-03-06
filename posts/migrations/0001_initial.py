# Generated by Django 3.0.3 on 2020-09-16 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('pst_id', models.AutoField(primary_key=True, serialize=False)),
                ('pst_data_criado', models.DateTimeField(auto_now=True)),
                ('pst_data_modificado', models.DateTimeField(auto_now_add=True)),
                ('pst_conteudo', models.TextField(max_length=1000)),
                ('pst_comentarios', models.TextField(max_length=400)),
            ],
        ),
    ]
