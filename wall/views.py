#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.template import RequestContext
from django.db.models import Sum

from models import *

def index(req):
    return render_to_response("index.html")

def minnesota(req):
    years = [2005, 2006, 2007, 2008]
    countries = Country.objects.all()
    countries_counts = []
    for country in countries:
        print country.name
        pos = country.purchaseorder_set
        totals = []
        smalls = []
        smalls_ratios = []
        mediums = []
        mediums_ratios = []
        larges = []
        larges_ratios = []

        for year in years:
            for month in range(13)[1:]:
                pos_mo = pos.filter(issue_date__year=year, issue_date__month=month)
                #po_amt = pos_mo.filter(new_book_g='A').aggregate(Sum('amount_usd'))['amount_usd__sum']
                total =  pos_mo.count()
                totals.append(total)
                small = pos_mo.filter(new_book_g='A').count()
                smalls.append(small)
                medium = pos_mo.filter(new_book_g='B').count()
                mediums.append(medium)
                large = pos_mo.filter(new_book_g='C').count()
                larges.append(large)
                if total != 0:
                    smalls_ratios.append( int((float(small)/float(total))*100) )
                    mediums_ratios.append( int((float(medium)/float(total))*100) )
                    larges_ratios.append( int((float(large)/float(total))*100) )
                else:
                    smalls_ratios.append(0)
                    mediums_ratios.append(0)
                    larges_ratios.append(0)

        #countries_counts.update({country.name:{"small":small, "medium":medium, "large":large}})
        countries_counts.append({"name":str(country.name), "smalls_ratios":smalls_ratios, "smalls":smalls, "mediums_ratios":mediums_ratios, "mediums":mediums, "larges_ratios":larges_ratios, "larges":larges, "totals":totals})
    print countries_counts
    return render_to_response("index.html", {"minnesota":countries_counts})

def show_tree(req):
    return render_to_response("tree.html")

def calc_tree(req):
    regs = Region.objects.all()
    cats = Category.objects.all()
    regs_cats = {}
    for reg in regs:
        print reg.name
        reg_cats = {}
        for cat in cats:
            num = cat.purchaseorder_set.filter(country__region=reg).count()
            reg_cats.update({str(cat.name):num})
        regs_cats.update({str(reg.name):reg_cats})
        print reg_cats
    print regs_cats
    return render_to_response("tree.html")

def prep_voyager(req):
    # var years = []
    # var jobs = {
    # "category" : { 'region' : [], 'anotherregion' : [] },
    # ...
    # }
    years = [2005, 2006, 2007, 2008]
    regs = Region.objects.all()
    cats = Category.objects.all()
    cats_regs = {}
    for cat in cats:
        print cat.name
        cat_regs = {}
        for reg in regs:
            print reg.name
            count = []
            for year in years:
                for month in range(13)[1:]:
                    num = PurchaseOrder.objects.filter(country__region=reg,\
                        issue_date__year=year, issue_date__month=month,\
                        category=cat).count()
                    count.append(num)
            cat_regs.update({str(reg.name):count})
        cats_regs.update({str(cat.name):cat_regs})
    print cats_regs
    return render_to_response("voyager.html")

def show_voyager(req):
    return render_to_response("voyager.html")
