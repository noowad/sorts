from __future__ import print_function
import numpy as np
import time
import inspect
from sort import *
from plot import plot


def main():
    methods = {'insert_sort': insert_sort, 'bubble_sort': bubble_sort, 'selection_sort': selection_sort,
               'quick_sort': quick_sort, 'merge_sort': merge_sort, 'heap_sort': heap_sort, 'shell_sort': shell_sort,
               'counting_sort': counting_sort, 'radix_sort': radix_sort, 'bucket_sort': bucket_sort}
    method_time = {}
    for method_name in methods:
        elapsed_times = 0
        for i in range(100):
            np.random.seed(seed=i)
            datas = list(np.random.randint(0, 500, 1000))
            start = time.time()
            methods[method_name](datas)
            end = time.time()
            elapsed_times += end - start
        print("{0} mean_elapsed_time:{1}".format(method_name, elapsed_times / 100) + "[sec]")
        method_time[method_name[:-5]] = round(elapsed_times, 3)
    plot(method_time)


if __name__ == "__main__":
    main()
