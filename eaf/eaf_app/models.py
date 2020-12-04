# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class ChemicalElement(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chemical_element'


class ChemicalCompositon(models.Model):
    element = models.ForeignKey('ChemicalElement', models.DO_NOTHING, blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    commodity = models.ForeignKey('CommodityProperties', models.DO_NOTHING, blank=True, null=True,related_name='chemical_composition')

    class Meta:
        managed = False
        db_table = 'chemical_compositon'


class CommodityProperties(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    inventory = models.CharField(max_length=45, blank=True, null=True)
    price = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commodity_properties'