# coding: utf-8
import csv

f = open('Rd2_pratice_1_total.csv','r')
reader = csv.reader(f)
for row in reader:
    print(row)

f.close()