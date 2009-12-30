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


from wall.models import *

def import_csv(args):

    # use codecs.open() instead of open() so all characters are utf-8 encoded
    # BEFORE we start dealing with them (just in case)
    # rU option is for universal-newline mode which takes care of \n or \r etc
    csvee = codecs.open("purchaseOrders.csv", "rU", encoding='utf-8', errors='ignore')

    # sniffer attempts to guess the file's dialect e.g., excel, etc
    dialect = csv.Sniffer().sniff(csvee.read(1024))
    # for some reason, sniffer was finding '"'
    dialect.quotechar = '"'
    csvee.seek(0)
    # DictReader uses first row of csv as key for data in corresponding column
    reader = csv.DictReader(csvee, dialect=dialect, delimiter=",", quoting=csv.QUOTE_ALL, doublequote=True)

    try:
        print 'begin rows'
        po_count = 0
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
            if has_datum(row, 'PO_OOI_REGION'):
                region, created = Region.objects.get_or_create(name=row['PO_OOI_REGION'])

                if has_datum(row, 'PO_OOI_COUNTRY'):
                    country, c_created = Country.objects.get_or_create(name=row['PO_OOI_COUNTRY'])
                    if c_created:
                        country.region = region
                        country.save()
                    if has_datum(row, 'CATEGORY_DESC'):
                        try:
                            category, created = Category.objects.get_or_create(name=row['CATEGORY_DESC'])
                        except Exception, e:
                            print 'BANG category:'
                            print e
                            print po_count
                            print row
                            continue

                        if has_data(row, ['SUPPLIER_COUNTRY', 'SUPPLIER_NAME']):
                            try:
                                supplier_country, created = Country.objects.get_or_create(name=row['SUPPLIER_COUNTRY'])
                                supplier, created  = Supplier.objects.get_or_create(name=row['SUPPLIER_NAME'], country=supplier_country)
                            except Exception, e:
                                print 'BANG supplier:'
                                print e
                                print po_count
                                print row
                                continue

                            if has_data(row, ['MATERIAL_TYPE', 'MATERIAL']):
                                try:
                                    material, created = Material.objects.get_or_create(name=row['MATERIAL'], material_type=row['MATERIAL_TYPE'])
                                except Exception, e:
                                    print 'BANG material:'
                                    print e
                                    print po_count
                                    print row
                                    continue
                                try:
    # [1] "ProMS.uid"                  "PO_TYPE"                   
    # [3] "MATERIAL_TYPE"              "Item.Line.Value"           
    # [5] "Old.Book.G"                 "New.Book.G"                
    # [7] "CATEGORY_DESC"              "MATERIAL"                  
    # [9] "MATERIAL_ADDITIONAL_INFO"   "PO_REFERENCE"              
    #[11] "PO_ISSUE_DATE"              "PO_DELIVERY_DATE"          
    #[13] "TAD"                        "TAFD"                      
    #[15] "BUDGET_YEAR"                "SUPPLIER_COUNTRY"          
    #[17] "SUPPLIER_NAME"              "QUANTITY_ORDERED"          
    #[19] "UNIT_PRICE..US..."          "PO_AMOUNT_USD"             
    #[21] "PO.Total.Value"             "Fraction.of.Total.PO.Value"
    #[23] "PO_OOI_COUNTRY"             "PO_OOI_REGION"             
    #[25] "X"                          "X.1"                       
    #[27] "Columns.introduced.by.us"   "Columns.from.ProMS"        
    #[29] "X.2" 
                                    try:
                                        new_purchase = Purchase(material=material,\
                                            unit_price=D(row['UNIT_PRICE (US $)']),\
                                            quantity=D(row['QUANTITY_ORDERED']),\
                                            supplier=supplier)
                                        new_purchase.save()
                                    except Exception, e:
                                        print 'BANG purchase:'
                                        print e
                                        print po_count
                                        print row
                                        continue

                                    def format_date(datestr):
                                        # expecting MM/DD/YY
                                        if datestr is not None:
                                            if datestr != '':
                                                month, day, year = datestr.split('/')
                                                millenium = '20'
                                                real_year = millenium + year
                                                return datetime.date(month=int(month),\
                                                    day=int(day), year=int(real_year))
                                            else:
                                                return None
                                        else:
                                            return None

                                    try:
                                        clean_issue_date = format_date(row['PO_ISSUE_DATE'])
                                        clean_delivery_date = format_date(row['PO_DELIVERY_DATE'])
                                        clean_tad = format_date(row['TAD'])
                                        clean_tafd = format_date(row['TAFD'])
                                    except Exception, e:
                                        print 'BANG dates:'
                                        print e
                                        print po_count
                                        print row
                                        continue

                                    # expecting -DD.DD%
                                    # chop off % and cast as decimal
                                    try:
                                        clean_fraction = D(row['Fraction of Total PO Value'][:-1])
                                    except Exception, e:
                                        print 'BANG fraction:'
                                        print e
                                        print po_count
                                        print row
                                        continue

                                    try:
                                        new_po = PurchaseOrder(country=country,\
                                            issue_date=clean_issue_date,\
                                            delivery_date=clean_delivery_date,\
                                            tad=clean_tad, tafd=clean_tafd,\
                                            reference=row['PO_REFERENCE'],\
                                            type=row['PO_TYPE'],\
                                            total_value=D(row['PO Total Value']),\
                                            fraction_of_tv=D(clean_fraction),\
                                            amount_usd=D(row['PO_AMOUNT_USD']),\
                                            budget_year=int(row['BUDGET_YEAR']),\
                                            item_line_value=row['Item Line Value'][2],\
                                            old_book_g=row['Old Book G'][2],\
                                            new_book_g=row['New Book G'][2],\
                                            category=category,\
                                            proms_uid=row['ProMS uid'],\
                                            additional_info=row['MATERIAL_ADDITIONAL_INFO'],\
                                            purchase=new_purchase)
                                        new_po.save()
                                        po_count += 1
                                        if po_count % 400 == 0:
                                            print(po_count)
                                    except Exception, e:
                                        print 'BANG po:'
                                        print e
                                        print po_count
                                        print row
                                        continue

                                except Exception, e:
                                    print(e)
                                    print po_count
                                    print row
                                    continue
                else:
                    print 'NO COUNTRY'
                    continue
            continue


    except csv.Error, e:
        # TODO handle this error?
        print('%d : %s' % (reader.reader.line_num, e))


if __name__ == "__main__":
    import_csv(sys.argv) 
