import timeit
from numpy import random
import seaborn as sns
import pandas as pd


# Insertion Sort
def insertion_sort(data_):
    data = data_.copy()
    for i in range(1, len(data)):
        cur = data[i]
        j = i - 1
        while j >= 0 and cur < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = cur
    return data


# Merge Sort
def merge_sort(data):
    def merge(left, right):
        res = []
        l_ix = 0
        r_ix = 0
        l_len = len(left)
        r_len = len(right)

        while l_ix < l_len and r_ix < r_len:
            if left[l_ix] <= right[r_ix]:
                res.append(left[l_ix])
                l_ix += 1
            else:
                res.append(right[r_ix])
                r_ix += 1

        while l_ix < l_len:
            res.append(left[l_ix])
            l_ix += 1

        while r_ix < r_len:
            res.append(right[r_ix])
            r_ix += 1

        return res

    if len(data) <= 1:
        return data

    cur = len(data) // 2
    l_data = data[:cur]
    r_data = data[cur:]

    return merge(merge_sort(l_data), merge_sort(r_data))


# Tim Sort
def tim_sort(data):
    data.sort()
    return data


def tim_sort_copy(data):
    data_ = data.copy()
    data_.sort()
    return data_


def tim_sorted(data):
    return sorted(data)


def is_sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True


def prepare_test_data(n_list, n_iter=4):
    test_data = {}
    for n in n_list:
        test_data[n] = random.randint(0xFFFF, size=(n_iter, n))
    return test_data


FUNCTIONS = {
    "InsertionSort": insertion_sort,
    "MergeSort": merge_sort,
    "TimSorted": sorted,
    "TimSort": tim_sort,
    "TimSortCopy": tim_sort_copy,
}


def test_functions(f_list, n_list, print_res=False):
    n_iter = 4
    data_set = prepare_test_data(n_list, n_iter)
    res = {}

    if print_res:
        print(f"| {'Sort method':^14} | {' | '.join([f"{str(n):^8}" for n in n_list])} |")
        print(f"|{'-'*16}" + f"|{'-'*10}" * (len(n_list)) + "|")

    for f_name in f_list:
        fn = FUNCTIONS[f_name]
        f_name_to_print = f_name
        measured_time = []
        for test in data_set:
            cumul_time = 0
            data_ = data_set[test]
            for i in range(n_iter):
                d = data_[i].copy()
                if len(d) > 1 and is_sorted(d):
                    raise Exception(
                        "data is sorted, the test will not be representative"
                    )
                cumul_time += timeit.timeit(lambda: fn(d), number=1)
            measured_time.append(cumul_time / n_iter)
        if print_res:
            print(f"| {f_name_to_print:^14} | {' | '.join([f"{n:^8.6f}" for n in measured_time])} |")
        res[f_name] = measured_time

    if print_res:
        print("\n")

    return pd.DataFrame(res)


def main():
    f_list = [
        "InsertionSort",
        "MergeSort",
        "TimSorted",
        "TimSort",
        "TimSortCopy",
    ]
    n_list = [i * 100 for i in range(16)]
    res = test_functions(f_list, n_list, True)
    # print(res)
    # sns.lineplot(res)

    f_list = [
        "MergeSort",
        "TimSorted",
        "TimSort",
        "TimSortCopy",
    ]
    n_list = [i * 10000 for i in range(16)]
    res = test_functions(f_list, n_list, True)
    # print(res)
    # sns.lineplot(res)

    f_list = [
        "TimSorted",
        "TimSort",
        "TimSortCopy",
    ]
    n_list = [i * 100_000 for i in range(16)]
    res = test_functions(f_list, n_list, True)
    # print(res)
    # sns.lineplot(res)

    f_list = [
        "InsertionSort",
        "MergeSort",
        "TimSorted",
        "TimSort",
        "TimSortCopy",
    ]
    n_list = [2**i for i in range(16)]
    res = test_functions(f_list, n_list, True)
    # print(res)
    # sns.lineplot(res)


if __name__ == "__main__":
    main()
