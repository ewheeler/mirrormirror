#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 coding=utf-8
import sys
import os

import codecs
import csv
import datetime
from decimal import Decimal as D

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.management import setup_environ

try:
    import settings
    setup_environ(settings)
except:
    sys.exit("No settings found")


from bigsky.models import *

def import_csv(args):

    # use codecs.open() instead of open() so all characters are utf-8 encoded
    # BEFORE we start dealing with them (just in case)
    # rU option is for universal-newline mode which takes care of \n or \r etc
    csvee = codecs.open("bigsky/static/data/UNdata_Export_20100325_114259171_cellphones_per_100.csv", "rU", encoding='utf-8', errors='ignore')

    # sniffer attempts to guess the file's dialect e.g., excel, etc
    dialect = csv.Sniffer().sniff(csvee.read(1024))
    # for some reason, sniffer was finding '"'
    dialect.quotechar = '"'
    csvee.seek(0)
    # DictReader uses first row of csv as key for data in corresponding column
    reader = csv.DictReader(csvee, dialect=dialect, delimiter=",", quoting=csv.QUOTE_ALL, doublequote=True)

    try:
        print 'begin rows'
        count = 0
        errors = []
        for row in reader:
            def has_datum(row, key):
                if row.has_key(key):
                    if row[key] != "":
                        return True
                return False

            def has_data(row, key_list):
                if False in [has_datum(row, key) for key in key_list]:
                    return False
                else:
                    return True

            def error(row):
                if row['Country or Area'] not in errors:
                    errors.append(row['Country or Area'])

            def nevermind(row):
                errors.remove(row['Country or Area'])

            if has_datum(row, 'Country or Area'):
                #print row['Country or Area']
                try:
                    country = Country.objects.get(printable_name__istartswith=row['Country or Area'])
                except MultipleObjectsReturned:
                    error(row)
                    country = Country.objects.get(printable_name__iexact=row['Country or Area'])
                    nevermind(row)
                except ObjectDoesNotExist:
                    error(row)
                except Exception, e:
                    error(row)
                    print e
                
                if has_data(row, ['Year', 'Value']):
                    try:
                        d = CellphonesPer100(name='Cellphones per 100 population',country=country, year=row['Year'], value=row['Value'])
                        d.save()
                        count += 1
                    except Exception, e:
                        print e

            print errors
            continue


    except csv.Error, e:
        # TODO handle this error?
        print('%d : %s' % (reader.reader.line_num, e))


if __name__ == "__main__":
    import_csv(sys.argv) 
