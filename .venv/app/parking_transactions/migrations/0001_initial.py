# Generated by Django 3.2.25 on 2025-02-13 14:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.UUIDField(db_column='employee_id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('employee_name', models.CharField(db_column='employee_name', max_length=255, verbose_name='Employee Name')),
                ('employee_gender', models.IntegerField(choices=[(0, 'Female'), (1, 'Male')], db_column='employee_gender', default=0, verbose_name='Employee Gender')),
                ('employee_dept', models.CharField(db_column='employee_dept', default='TBA', editable=False, max_length=50)),
                ('employee_post', models.ForeignKey(db_column='employee_post', on_delete=django.db.models.deletion.CASCADE, related_name='employee_post', to='libraries.departmentpositions', verbose_name='Employee Position')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'tbl_employees',
            },
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('vehicle_id', models.AutoField(db_column='vehicle_id', editable=False, primary_key=True, serialize=False)),
                ('vehicle_plate', models.CharField(db_column='vehicle_plate', max_length=8)),
                ('vehicle_type', models.IntegerField(choices=[(0, 'CAR'), (1, 'MOTORCYCLE'), (2, 'BICYCLE'), (3, 'SCOOTER'), (4, 'E-BIKE')], db_column='vehicle_type', default=0)),
                ('vehicle_emp', models.ForeignKey(db_column='vehicle_emp_id', on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_emp', to='parking_transactions.employees', verbose_name='Vehicle Owner')),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'Vehicles',
                'db_table': 'tbl_vehicles',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('txn_id', models.AutoField(db_column='txn_id', editable=False, primary_key=True, serialize=False)),
                ('txn_state', models.IntegerField(choices=[(0, 'Parked'), (1, 'Reserved'), (3, 'In Transit'), (4, 'Charging')], db_column='txn_state', default=0)),
                ('txn_date', models.DateField(db_column='txn_date')),
                ('txn_created', models.DateTimeField(auto_now_add=True, db_column='txn_created')),
                ('txn_updated', models.DateTimeField(auto_now=True, db_column='txn_updated')),
                ('txn_plate', models.ForeignKey(db_column='txn_plate_id', on_delete=django.db.models.deletion.CASCADE, related_name='txn_plate', to='parking_transactions.vehicles')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'db_table': 'tbl_transactions',
            },
        ),
    ]
