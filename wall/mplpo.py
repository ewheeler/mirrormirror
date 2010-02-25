import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.colors as mcol
import matplotlib.cm as cm
from matplotlib.patches import Polygon

from wall.models import *

def get_all_amts():
    print 'getting PO amounts...'
    all_amount_usd = PurchaseOrder.objects.values_list('amount_usd', flat=True).order_by('amount_usd')
    print 'found %s, converting to floats...' % len(all_amount_usd)
    all_amount_usd_f = [float(x) for x in all_amount_usd if x > 0.0]
    print 'converted %s amounts!' % len(all_amount_usd_f)
    all = all_amount_usd_f[0:362549]
    return all

def get_regional_amts(name=True):
    all = []
    regs = Region.objects.all()
    for reg in regs:
        if reg.name is not None:
            if reg.name not in ['2006']:
                print 'getting PO amounts for %s' % reg.name
                ramts = PurchaseOrder.objects.values_list('amount_usd',\
                    flat=True).filter(country__region=reg).order_by('-amount_usd')
                ramts_f = [float(x) for x in ramts if x > 0.0]
                if name:
                    ramts_f.append(reg.name)
                all.append(ramts_f)
    return all

def get_country_amts(reg, name=True):
    all = []
    region = Region.objects.get(name__iexact=reg)
    countries = Country.objects.filter(region=region)
    for country in countries:
        print 'getting PO amounts for %s' % country.name
        camts = PurchaseOrder.objects.values_list('amount_usd',\
                flat=True).filter(country=country).order_by('-amount_usd')
        camts_f = [float(x) for x in camts if x > 0.0]
        if name:
            camts_f.append(country.name)
        if len(camts_f) > 1:
            all.append(camts_f)
    return all

def get_category_amts(country_name, name=True):
    all = []
    country = Country.objects.get(name__iexact=country_name)
    cats = Category.objects.all()
    for cat in cats:
        print 'geting %s PO amounts for %s' % (country.name, cat.name)
        camts = PurchaseOrder.objects.values_list('amount_usd',\
                flat=True).filter(country=country).filter(category=cat)\
                .order_by('-amount_usd')
        camts_f = [float(x) for x in camts if x > 0.0]
        if name:
            camts_f.append(cat.name)
        if len(camts_f) > 1:
            all.append(camts_f)
    return all

def get_stats(amts):
    for amt in amts:
        print '%s' % amt.pop()
        print 'mean:   %s' % np.mean(amt)
        print 'median: %s' % np.median(amt)
        print 'std:    %s' % np.std(amt)
        print 'var:    %s' % np.var(amt)

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

def make_boxplot(amounts, height=None):
    fig = plt.figure(figsize=(10,6))
    fig.canvas.set_window_title('Boxplots')
    ax1 = fig.add_subplot(111)
    plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

    amts = list(amounts)

    names = [str(lst.pop()) for lst in amts]

    bp = plt.boxplot(amts, notch=0, sym='+', vert=1, whis=1.5)
    plt.setp(bp['boxes'], color='black')
    plt.setp(bp['whiskers'], color='black')
    plt.setp(bp['fliers'], color='red', marker='+')

    # Add a horizontal grid to the plot, but make it very light in color
    # so we can use it for reading data values but not be distracting
    ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                alpha=0.5)

    # Hide these grid behind plot objects
    ax1.set_axisbelow(True)
    ax1.set_title('Comparison of PO volumes')
    ax1.set_ylabel('Value (amount USD) of PO')

    # Now fill the boxes with desired colors
    boxColors = ['royalblue']
    numBoxes = len(amts)
    medians = range(numBoxes)
    # for shading 'Blues'
    counts = [len(a) for a in amts]
    ndcounts = np.array(counts)
    norm = mcol.normalize(np.amin(ndcounts), np.amax(ndcounts))
    ncounts = [norm(c) for c in counts]
    #cmap = plt.get_cmap('Blues')

    for i in range(numBoxes):
        box = bp['boxes'][i]
        boxX = []
        boxY = []
        for j in range(5):
            boxX.append(box.get_xdata()[j])
            boxY.append(box.get_ydata()[j])
        boxCoords = zip(boxX,boxY)
        # Alternate between Dark Khaki and Royal Blue
        #k = i % 2
        # TODO shade boxes by len(amt)
        boxPolygon = Polygon(boxCoords, facecolor=cm.Blues(ncounts[i]))
        #boxPolygon = Polygon(boxCoords, facecolor=boxColors[0])
        ax1.add_patch(boxPolygon)
        # Now draw the median lines back over what we just filled in
        med = bp['medians'][i]
        medianX = []
        medianY = []
        for j in range(2):
            medianX.append(med.get_xdata()[j])
            medianY.append(med.get_ydata()[j])
            plt.plot(medianX, medianY, 'k')
            medians[i] = medianY[0]
        # Finally, overplot the sample averages, with horixzontal alignment
        # in the center of each box
        plt.plot([np.average(med.get_xdata())], [np.average(amts[i])],
                color='w', marker='*', markeredgecolor='k')


    # Set the axes ranges and axes labels
    ax1.set_xlim(0.5, numBoxes)
    top = height 
    bottom = -5
    ax1.set_ylim(bottom, top)
    xtickNames = plt.setp(ax1, xticklabels=names)
    plt.setp(xtickNames, rotation=90, fontsize=8)

    # Due to the Y-axis scale being different across samples, it can be
    # hard to compare differences in medians across the samples. Add upper
    # X-axis tick labels with the sample medians to aid in comparison
    # (just use two decimal places of precision)
    pos = np.arange(numBoxes)+1
    #upperLabels = [str(np.round(s, 2)) for s in medians]
    weights = ['bold', 'semibold']
    for tick,label in zip(range(numBoxes),ax1.get_xticklabels()):
        ax1.text(pos[tick], top-(top*0.05), str(len(amts[tick])),
                horizontalalignment='center', size='8', weight=weights[0],
                color=boxColors[0])

    # Finally, add a basic legend
    plt.figtext(0.75, 0.08, 'Interquartile range (25-75%) of POs',
    backgroundcolor=boxColors[0],
            color='black', weight='roman', size='x-small')
    plt.figtext(0.75, 0.045, 'Number of POs',
    backgroundcolor='silver',
            color=boxColors[0], weight='semibold', size='x-small')
    plt.figtext(0.75, 0.015, '*', color='white', backgroundcolor='silver',
            weight='roman', size='medium')
    plt.figtext(0.765, 0.013, ' Average PO amount (USD)', color='black', weight='roman',
            size='x-small')

    plt.axis([0, len(amts)+1, 0, height]) 
    plt.show()
