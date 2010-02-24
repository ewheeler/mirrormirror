from wall.models import *
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def get_all_amounts():
    print 'getting PO amounts...'
    all_amount_usd = PurchaseOrder.objects.values_list('amount_usd', flat=True).order_by('amount_usd')
    print 'found %s, converting to floats...' % len(all_amount_usd)
    all_amount_usd_f = [float(x) for x in all_amount_usd]
    print 'converted %s amounts!' % len(all_amount_usd_f)
    all = all_amount_usd_f[0:362549]
    return all


def make_hist(amts, line=False):
    min = amts[0]
    max = amts[-1]

    steps = range(0,20000,200)

    n, bins, patches = plt.hist(amts, steps, normed=0, facecolor='green', alpha=0.75)
    #n, bins, patches = plt.hist(amts, [0,200,400,600,800,1000,1200,1400,1600,1800,2000,20000], normed=0, facecolor='green', alpha=0.75)
    #n, bins, patches = plt.hist(all, [0,200,400,600,800,1000,1200,1400,1600,1800,2000,2000000], normed=0, facecolor='green', alpha=0.75)

    def best_fit():
        mu, sigma = 100, 15
        y = mlab.normpdf( bins, mu, sigma)
        l = plt.plot(bins, y, 'r--', linewidth=3)

    if line:
        best_fit()

    plt.grid(True)
    plt.xlabel('PO Amount USD')
    plt.ylabel('Number of POs')
    plt.show()
