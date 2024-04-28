import numpy as np
import random as rd
import time

l1 = [23,104,5,190,8,7,-3]
l2 = []
l3 = [rd.randint(0,10000) for x in range(1000000)]


def sort_lists_without_numpy(list, time):
    start = time.time()
    sortedList = [i[0] for i in sorted(enumerate(list), key=lambda x:x[1])]
    time = time.time() - start
    print(sortedList)
    return time

def sort_lists_with_numpy(list, time):
    start = time.time()
    sortedList = np.argsort(list).tolist()
    time = time.time() - start
    print(sortedList)
    return time

def sort_lists(list, time):
    if list == type(None) or len([x for x in list if not str(x).strip("-").isdigit()]) > 0 :
        raise TypeError("input is empty or not numerical")
    
    print("without numpy:")
    time_without_numpy = sort_lists_without_numpy(list, time)
    print("with numpy:")
    time_with_numpy = sort_lists_with_numpy(list, time)

    if time_without_numpy > time_with_numpy:
        print("Sort with numpy was faster: without numpy " + str(time_without_numpy) + ", with numpy: " + str(time_with_numpy))
    elif time_without_numpy < time_with_numpy:
        print("Sort without numpy was faster: without numpy " + str(time_without_numpy) + ", with numpy: " + str(time_with_numpy))
    else:
        print("Both sorting functions were equally fast: without numpy " + str(time_without_numpy) + ", with numpy: " + str(time_with_numpy))


print("list 1")
sort_lists(l1, time)
print("list 2")
sort_lists(l2, time)
print("list 3")
sort_lists(l3, time)
