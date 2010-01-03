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
    countries = Country.objects.filter(name__istartswith="U")
    countries_counts = []
    for country in countries:
        print country.name
        pos = country.purchaseorder_set
        small = []
        medium = []
        large = []

        for year in years:
            for month in range(13)[1:]:
                pos_mo = pos.filter(issue_date__year=year, issue_date__month=month)
                #po_amt = pos_mo.filter(new_book_g='A').aggregate(Sum('amount_usd'))['amount_usd__sum']
                small.append(pos_mo.filter(new_book_g='A').count())
                medium.append(pos_mo.filter(new_book_g='B').count())
                large.append(pos_mo.filter(new_book_g='C').count())

        #countries_counts.update({country.name:{"small":small, "medium":medium, "large":large}})
        countries_counts.append({"name":str(country.name), "values": {"small":small, "medium":medium, "large":large}})
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
