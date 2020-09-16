# Generated by Django 3.0.3 on 2020-09-16 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projetos', '0001_initial'),
        ('posts', '0001_initial'),
        ('organizacao', '0001_initial'),
        ('equipe', '0002_equipe_eqp_criador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usr_id', models.AutoField(primary_key=True, serialize=False)),
                ('usr_nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('usr_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('usr_cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('usr_estado', models.CharField(max_length=2, verbose_name='Estado (UF)')),
                ('usr_area', models.CharField(max_length=20, verbose_name='Area de Atuação')),
                ('usr_cargo', models.CharField(max_length=30, verbose_name='Cargo')),
                ('usr_email', models.EmailField(max_length=254)),
                ('usr_telefone', models.IntegerField()),
                ('usr_senha', models.CharField(max_length=100)),
                ('usr_avatar', models.ImageField(height_field=400, upload_to=None, width_field=400)),
                ('usr_capa', models.ImageField(upload_to=None)),
                ('usr_bio', models.TextField(max_length=240)),
                ('usr_plano', models.BooleanField(default=False)),
                ('usr_equipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='equipe.Equipe')),
                ('usr_likes', models.ManyToManyField(related_name='likes', to='organizacao.Organizacao')),
                ('usr_matchs', models.ManyToManyField(to='organizacao.Organizacao')),
                ('usr_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
                ('usr_projeto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projetos.Projeto')),
            ],
        ),
    ]
