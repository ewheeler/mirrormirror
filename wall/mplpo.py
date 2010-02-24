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

def make_hist(amts, max=20000, step=200, htype=None):

    steps = range(0,max,step)
    pretty = ['red','green','blue','orange','yellow','springgreen',\
                'slategray','fuchsia']

    if htype == 'barstacked':
        print 'barstacked!'
        for amt_list in amts:
            n, bins, patches = plt.hist(amt_list[:-1], steps, normed=0,\
                histtype='barstacked', label=amt_list[-1],\
                facecolor=pretty.pop())
    else:
        print 'plain'
        n, bins, patches = plt.hist(amts, steps, normed=0, alpha=0.85, histtype='bar')

    plt.grid(True)
    plt.xlabel('PO Amount USD')
    plt.ylabel('Number of POs')
    plt.axis([0,max,0,40000])
    plt.legend()
    plt.show()
