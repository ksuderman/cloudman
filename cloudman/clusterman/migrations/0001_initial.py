# Generated by Django 2.2.10 on 2020-02-17 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cloudlaunch', '0001_initial'),
        ('djcloudbridge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMAutoScaler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('vm_type', models.CharField(max_length=200)),
                ('min_nodes', models.IntegerField(default=0)),
                ('max_nodes', models.IntegerField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'Cluster Autoscaler',
                'verbose_name_plural': 'Cluster Autoscalers',
            },
        ),
        migrations.CreateModel(
            name='CMCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=60)),
                ('cluster_type', models.CharField(max_length=255)),
                ('autoscale', models.BooleanField(default=True, help_text='Whether autoscaling is activated')),
                ('_connection_settings', models.TextField(blank=True, db_column='connection_settings', help_text='External provider specific settings for this cluster.', max_length=16384, null=True)),
            ],
            options={
                'verbose_name': 'Cluster',
                'verbose_name_plural': 'Clusters',
            },
        ),
        migrations.CreateModel(
            name='CMClusterNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('autoscaler', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nodegroup', to='clusterman.CMAutoScaler')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='node_list', to='clusterman.CMCluster')),
                ('deployment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cm_cluster_node', to='cloudlaunch.ApplicationDeployment')),
            ],
            options={
                'verbose_name': 'Cluster Node',
                'verbose_name_plural': 'Cluster Nodes',
            },
        ),
        migrations.AddField(
            model_name='cmautoscaler',
            name='cluster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autoscaler_list', to='clusterman.CMCluster'),
        ),
        migrations.AddField(
            model_name='cmautoscaler',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autoscaler_list', to='djcloudbridge.Zone'),
        ),
        migrations.AlterUniqueTogether(
            name='cmautoscaler',
            unique_together={('cluster', 'name')},
        ),
    ]
