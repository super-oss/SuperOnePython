import csv, sys, os
datalist = list(['aho', 'アホ', 'fool'], ['roman', '日本語', 'eng'])
with open('downloads/test.csv', 'x', newline='') as csv1:
    write = csv.writer(csv1, csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for newrow in datalist:
        write.writerow(newrow)
