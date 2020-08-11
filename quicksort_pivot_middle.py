import csv
import time
import psutil
import os

def quick_sort(int_arr):
    if len(int_arr) <= 1 : return int_arr
    pivot = int_arr[ len(int_arr)//2]
    bigger_arr = [ big for big in int_arr[1:] if big > pivot]
    lesser_arr = [ less for less in int_arr[1:] if less < pivot]
    return quick_sort(lesser_arr) + [pivot] + quick_sort(bigger_arr)

print("[!]--- Quick Sort Start ---[!]")
memory_usage_dict = dict(psutil.virtual_memory()._asdict())
memory_usage_percent = memory_usage_dict['percent']
print(f"BEFORE CODE: memory_usage_percent: {memory_usage_percent}%")
pid = os.getpid()
current_process = psutil.Process(pid)
current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
f = open('output.csv', 'r')
int_arr = []
with f:
    reader = csv.reader(f)
    for row in reader:
        for e in row:
            int_arr.append(int(e))

start = time.time()
int_arr = quick_sort(int_arr)

memory_usage_dict = dict(psutil.virtual_memory()._asdict())
memory_usage_percent = memory_usage_dict['percent']
print(f"AFTER  CODE: memory_usage_percent: {memory_usage_percent}%")
pid = os.getpid()
current_process = psutil.Process(pid)
current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")

print("[!] Learning Time : " , time.time() - start ,"[!]")

f = open('output.csv', 'w', newline="")
for arr in int_arr:
    writer = csv.writer(f)
    writer.writerow([arr])

f.close()
