from wall.models import *
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def get_all_amts():
    print 'getting PO amounts...'
    all_amount_usd = PurchaseOrder.objects.values_list('amount_usd', flat=True).order_by('amount_usd')
    print 'found %s, converting to floats...' % len(all_amount_usd)
    all_amount_usd_f = [float(x) for x in all_amount_usd if x > 0.0]
    print 'converted %s amounts!' % len(all_amount_usd_f)
    all = all_amount_usd_f[0:362549]
    return all

def get_regional_amts():
    all = []
    regs = Region.objects.all()
    for reg in regs:
        if reg.name is not None:
            if reg.name not in ['2006']:
                print 'getting PO amounts for %s' % reg.name
                ramts = PurchaseOrder.objects.values_list('amount_usd',\
                    flat=True).filter(country__region=reg).order_by('amount_usd')
                ramts_f = [float(x) for x in ramts if x > 0.0]
                ramts_f.append(reg.name)
                all.append(ramts_f)
    return all

def get_country_amts(reg):
    all = []
    region = Region.objects.get(name__iexact=reg)
    countries = Country.objects.filter(region=region)
    for country in countries:
        print 'getting PO amounts for %s' % country.name
        camts = PurchaseOrder.objects.values_list('amount_usd',\
                flat=True).filter(country=country).order_by('amount_usd')
        camts_f = [float(x) for x in camts if x > 0.0]
        camts_f.append(country.name)
        all.append(camts_f)
    return all

def get_category_amts(country_name):
    all = []
    country = Country.objects.get(name__iexact=country_name)
    cats = Category.objects.all()
    for cat in cats:
        print 'geting %s PO amounts for %s' % (country.name, cat.name)
        camts = PurchaseOrder.objects.values_list('amount_usd',\
                flat=True).filter(country=country).filter(category=cat)\
                .order_by('amount_usd')
        camts_f = [float(x) for x in camts if x > 0.0]
        camts_f.append(cat.name)
        all.append(camts_f)
    return all

def make_hist(amts, max=20000, step=200, htype=None, height=40000, legend=True):

    steps = range(0,max,step)
    cmap = plt.get_cmap('Paired', len(amts))

    if htype == 'barstacked':
        print 'barstacked!'
        for index, amt_list in enumerate(amts):
            n, bins, patches = plt.hist(amt_list[:-1], steps, normed=0,\
                histtype='barstacked', label=amt_list[-1],\
                facecolor=cmap(index))
    else:
        print 'plain'
        n, bins, patches = plt.hist(amts, steps, normed=0, alpha=0.85, histtype='bar')

    plt.grid(True)
    plt.xlabel('PO Amount USD')
    plt.ylabel('Number of POs')
    plt.axis([0,max,0,height])
    if legend:
        plt.legend()
    plt.show()
