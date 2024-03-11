import csv

d = [i for i in range(10, 100, 10)]

lst = open('dict.csv', 'w+')
csvreader = csv.writer(lst)
csvreader.writerow(d)
lst.close()
