from astropy.io import fits
import numpy as np
import sys

if len(sys.argv) < 3:
    print('Usage: %s standard.txt image.fits' % sys.argv[0])
    sys.exit()

f = open(sys.argv[1])
std = dict((k,v) for k, v in [x.replace('\n', '').split(' = ') for x in f.readlines()])

hdr = fits.getheader(sys.argv[2])
for k in std.keys():
    if std[k].endswith('M'):
        aux = '    MANDATORY     '
    elif std[k].endswith('R'):
        aux = '    RECOMMENDED   '
    else:
        aux = '    OPTIONAL      '
    if k in hdr.keys():
        print('[OK] '+aux+k)
    else:
        print('[NOK]'+aux+k)
