#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=80)
    printable_name = models.CharField(max_length=80)
    iso_code = models.CharField(max_length=2, primary_key=True)
    iso3_code = models.CharField(max_length=3, blank=True, null=True)
    numerical_code = models.PositiveIntegerField(blank=True, null=True)

class Region(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)

class DatasetBase(models.Model):
    name = models.CharField(max_length=160, blank=True, null=True)
    country = models.ForeignKey(Country, blank=True, null=True)

    class Meta:
        abstract = True

class InternetPer100(DatasetBase):
    year = models.PositiveIntegerField(max_length=10, blank=True, null=True)
    value = models.CharField(max_length=30, blank=True, null=True)

class CellphonesPer100(DatasetBase):
    year = models.PositiveIntegerField(max_length=10, blank=True, null=True)
    value = models.CharField(max_length=30, blank=True, null=True)

class LogisticsPerformance(DatasetBase):
    year = models.PositiveIntegerField(max_length=10, blank=True, null=True)

    rank = models.CharField(max_length=30, blank=True, null=True)
    LPI = models.CharField(max_length=30, blank=True, null=True)
    customs = models.CharField(max_length=30, blank=True, null=True)
    infrastructure = models.CharField(max_length=30, blank=True, null=True)
    intl_shipments = models.CharField(max_length=30, blank=True, null=True)
    competence = models.CharField(max_length=30, blank=True, null=True)
    tracking_tracing = models.CharField(max_length=30, blank=True, null=True)
    timeliness = models.CharField(max_length=30, blank=True, null=True)
