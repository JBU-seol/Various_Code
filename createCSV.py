import csv
import random
import time

f = open('output.csv','w', encoding='utf-8', newline="")
writer = csv.writer(f)
start = time.time()
for i in range(1000000):
    writer.writerow([random.randint(0,1000000)])
f.close()
