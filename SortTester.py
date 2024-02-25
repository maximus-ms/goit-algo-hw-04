import timeit
from numpy import random
import matplotlib.pyplot as plt


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
        generate_data = True
        while generate_data:
            generate_data = False
            data = random.randint(0xFFFF, size=(n_iter, n))
            for i in range(n_iter):
                if len(data[i]) > 1 and is_sorted(data[i]):
                    generate_data = True
                    break
        test_data[n] = data
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
        measured_time = []
        for test in data_set:
            cumul_time = 0
            data_ = data_set[test]
            for i in range(n_iter):
                cumul_time += timeit.timeit(lambda: fn(data_[i].copy()), number=1)
            measured_time.append(cumul_time / n_iter)
        if print_res:
            print(f"| {f_name:^14} | {' | '.join([f"{n:^8.6f}" for n in measured_time])} |")
        res[f_name] = measured_time

    if print_res:
        print("\n")

    return res

def plot_results(test_results, n_list):
    plt.figure(figsize=(10, 6))
    for sort_func_name, times in test_results.items():
        plt.plot(n_list, times, label=sort_func_name)
    plt.xlabel('Array Length')
    plt.ylabel('Time (s)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    tests = [100, 10_000, 100_000]
    test_to_plot = tests[0]

    n_list = {}
    test_results = {}

    f_list = [
        "InsertionSort",
        "MergeSort",
        "TimSorted",
        "TimSort",
        "TimSortCopy",
    ]

    for i, test in enumerate(tests):
        n_list[test] = [i * test for i in range(16)]
        test_results[test] = test_functions(f_list[i:], n_list[test], True)

    plot_results(test_results[test_to_plot], n_list[test_to_plot])

    # n_list_pow2 = [2**i for i in range(15)]
    # test_results_pow2 = test_functions(f_list, n_list, True)
    # plot_results(test_results_pow2, n_list_pow2)


if __name__ == "__main__":
    main()
