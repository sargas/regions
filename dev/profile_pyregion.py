import pyregion
import glob

l = glob.glob('data/*.reg')

for f in l:
    #    print(f)
    if 'strip' in f or 'comment' in f:
        continue
    s = pyregion.open(str(f))
