#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)
    region = models.ForeignKey('Region', blank=True, null=True)
    # TODO add ISO and UN country codes

class Region(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)
    
class PurchaseOrder(models.Model):
    PO_TYPE_CHOICES = (
        ('X', 'X'),
        ('E', 'E'),
    )
    ITEM_LINE_VALUE_CHOICES = (
        ('A', '< 100'),
        ('B', '> 100'),
    )
    OLD_BOOK_G_CHOICES = (
        ('A', '< 500'),
        ('B', '500 - 1000'),
        ('C', '1000 - 2500'),
        ('D', '> 2500'),
    )
    NEW_BOOK_G_CHOICES = (
        ('A', '< 1000'),
        ('B', '1000 - 2500'),
        ('C', '> 2500'),
    )
    country = models.ForeignKey(Country)
    issue_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    tad = models.DateField(blank=True, null=True)
    tafd = models.DateField(blank=True, null=True)
    reference = models.CharField(max_length=160, blank=True, null=True)
    type = models.CharField(max_length=1, choices=PO_TYPE_CHOICES, blank=True, null=True)
    total_value = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    fraction_of_tv = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    amount_usd = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    budget_year = models.PositiveIntegerField(blank=True, null=True)
    item_line_value = models.CharField(max_length=1, choices=ITEM_LINE_VALUE_CHOICES, blank=True, null=True)
    old_book_g = models.CharField(max_length=1, choices=OLD_BOOK_G_CHOICES, blank=True, null=True)
    new_book_g = models.CharField(max_length=1, choices=NEW_BOOK_G_CHOICES, blank=True, null=True)
    category = models.ForeignKey('Category', blank=True, null=True)
    proms_uid = models.PositiveIntegerField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    purchase = models.ForeignKey('Purchase')

class Purchase(models.Model):
    material = models.ForeignKey('Material')
    unit_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # TODO some countries seem to order fractions of units (?)
    # things like books (i'm looking at you El Salvador..)
    #quantity = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    supplier = models.ForeignKey('Supplier', blank=True, null=True)

class Material(models.Model):
    # 243 of these
    MATERIAL_TYPE_CHOICES = (
        ('CO', 'CO'),
        ('NW', 'NW'),
        ('UN', 'UN'),
    )
    name = models.CharField(max_length=160, blank=True, null=True)
    material_type = models.CharField(max_length=2, choices=MATERIAL_TYPE_CHOICES, blank=True, null=True)

class Category(models.Model):
    # 26 of these
    name = models.CharField(max_length=160, blank=True, null=True)

class Supplier(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    country = models.ForeignKey(Country)
