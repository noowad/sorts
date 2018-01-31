# coding:utf-8
from __future__ import print_function
from math import log

def insert_sort(datas):
    if len(datas) <= 1:
        return datas
    else:
        for i in range(1, len(datas)):
            while i > 0 and datas[i] < datas[i - 1]:
                datas[i], datas[i - 1] = datas[i - 1], datas[i]
                i -= 1
        return datas


def bubble_sort(datas):
    if len(datas) <= 1:
        return datas
    else:
        for i in reversed(range(1, len(datas))):
            for j in reversed(range(0, len(datas[:i]) - 1)):
                if datas[i] < datas[j]:
                    datas[i], datas[j] = datas[j], datas[i]
        return datas


def selection_sort(datas):
    if len(datas) <= 1:
        return datas
    else:

        for i in range(0, len(datas) - 1):
            if i != 0:
                max_data = max(datas[:-i])
                max_index = datas[:-i].index(max_data)
                datas[max_index], datas[len(datas[:-i]) - 1] = datas[len(datas[:-i]) - 1], datas[max_index]
            else:
                max_data = max(datas)
                max_index = datas.index(max_data)
                datas[max_index], datas[len(datas) - 1] = datas[len(datas) - 1], datas[max_index]
        return datas


def quick_sort(datas):
    if len(datas) <= 1:
        return datas
    else:
        pivot = datas[len(datas) // 2]
        # better if use median
        smaller = []
        bigger = []
        for data in datas[:len(datas) / 2] + datas[(len(datas) / 2 + 1):]:
            if data < pivot:
                smaller.append(data)
            else:
                bigger.append(data)
        return quick_sort(smaller) + [pivot] + quick_sort(bigger)


def merge_sort(datas):
    if len(datas) <= 1:
        return datas
    else:
        left = datas[:len(datas) // 2]
        right = datas[len(datas) // 2:]

        left = merge_sort(left)
        right = merge_sort(right)
        return left, right
        # return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


def heap_sort(datas):
    datas_len = len(datas)
    # Build Max-Heap
    for i in range(datas_len // 2 - 1, -1, -1):
        heapify(datas, i, datas_len)
    # Recurrent
    for i in range(datas_len - 1, 0, -1):
        datas[0], datas[i] = datas[i], datas[0]
        heapify(datas, 0, i)
    return datas


def heapify(datas, index, heap_size):
    largest = index
    left_index = index * 2 + 1
    right_index = index * 2 + 2
    if left_index < heap_size and datas[left_index] > datas[largest]:
        largest = left_index
    if right_index < heap_size and datas[right_index] > datas[largest]:
        largest = right_index
    if largest != index:
        datas[largest], datas[index] = datas[index], datas[largest]
        heapify(datas, largest, heap_size)


def shell_sort(datas):
    gap = len(datas) // 2
    while gap > 0:
        for start_index in range(0, gap):
            for i in range(start_index + gap, len(datas), gap):
                current_value = datas[i]
                current_index = i

                while current_index >= gap and datas[current_index - gap] > current_value:
                    datas[current_index] = datas[current_index - gap]
                    current_index = current_index - gap

                datas[current_index] = current_value

        gap = gap // 2

    return datas


# non-comparison sorting O(n) and data>=0
def counting_sort(datas):
    max_value = max(datas)
    sorted_datas = [-1] * len(datas)
    counting_list = [0] * (max_value + 1)  # data>=0
    for data in datas:
        counting_list[data] += 1
    for i in range(len(counting_list) - 1):
        counting_list[i + 1] += counting_list[i]

    for data in reversed(datas):
        sorted_datas[counting_list[data] - 1] = data
        counting_list[data] -= 1

    return sorted_datas


# radix sort
def radix_sort(datas):
    base = 10  # 10進法

    def get_digit(number, digit, base):
        return (number // (base ** digit)) % base

    def counting_sort_with_digits(datas, digit, base):
        max_value = base - 1
        sorted_datas = [-1] * len(datas)
        counting_list = [0] * (max_value + 1)
        for data in datas:
            counting_list[get_digit(data, digit, base)] += 1
        for i in range(len(counting_list) - 1):
            counting_list[i + 1] += counting_list[i]
        for data in reversed(datas):
            sorted_datas[counting_list[get_digit(data, digit, base)] - 1] = data
            counting_list[get_digit(data, digit, base)] -= 1
        return sorted_datas

    max_digit = int(log(max(datas), base)) + 1
    for digit in range(0, max_digit):
        datas = counting_sort_with_digits(datas, digit, base)
    return datas


def bucket_sort(datas):
    buckets = [[] for i in range(len(datas))]
    for data in datas:
        bucket_index = data * len(datas) // (max(datas) + 1)
        buckets[bucket_index].append(data)
    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(quick_sort(bucket))
    return sorted_list
