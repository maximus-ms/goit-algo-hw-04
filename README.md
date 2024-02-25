# GoITNeo Algo HW-4

## Task
Compare three sorting algorithms: Insertion Sort, Merge Sort and Timsort based on their execution time. The analysis should be supported by empirical data obtained through testing the algorithms on different datasets. Empirically verify the theoretical complexity estimates of the algorithms, such as sorting on large arrays. Use the ```timeit``` module to measure the execution time of the algorithms.

## What we test
Let's compare next function:
 - ```InsertionSort``` - does not change an input data
 - ```MergeSort``` - does not change an input data
 - ```TimSorted``` - standard python function ```sorted()```, does not change an input data
 - ```TimSort``` - standard python list's method ```sort()```, DOES change an input data
 - ```TimSortCopy``` - standard python list's method ```sort()```, with copy an input data and applying ```sort()```

## How we test
1. Generate a data_set with:
    - different array size (for example number of elements ```[100, 200, 300, ..., 1500]```)
    - for each array size 4 data_sets (will help us to minimize an influence of how numbers are located in an array)
2. Each sort method get's a copy of the test data. It will give us the ability to test and compare mutable and immutable functions.
3. Measure an execution time of each method with each array size 4 times (one per data_set), and get an average value.
4. Limit a set of measured methods for different array sizes (optimization of test time):
    - ```InsertionSort, MergeSort, TimSorted, TimSort, TimSortCopy``` for size [100 .. 1500]
    - ```MergeSort, TimSorted, TimSort, TimSortCopy``` for size [10_000 .. 150_000]
    - ```TimSorted, TimSort, TimSortCopy``` for size [100_000 .. 1_500_000]
    - ```InsertionSort, MergeSort, TimSorted, TimSort, TimSortCopy``` for size $[2^{0},2^{1} .. 2^{15}]$

## Results
### Array size 100 .. 1500
|  Sort method   |    0     |   100    |   200    |   300    |   400    |   500    |   600    |   700    |   800    |   900    |   1000   |   1100   |   1200   |   1300   |   1400   |   1500   |
|----------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| InsertionSort  | 0.000008 | 0.000472 | 0.002441 | 0.004834 | 0.008213 | 0.012116 | 0.020150 | 0.024545 | 0.032844 | 0.048126 | 0.052597 | 0.065440 | 0.078873 | 0.096945 | 0.104877 | 0.120530 |
|   MergeSort    | 0.000006 | 0.000177 | 0.000370 | 0.000440 | 0.000607 | 0.000751 | 0.001033 | 0.001877 | 0.001965 | 0.002927 | 0.003344 | 0.002747 | 0.002206 | 0.002187 | 0.002278 | 0.002589 |
|   TimSorted    | 0.000011 | 0.000039 | 0.000067 | 0.000101 | 0.000145 | 0.000180 | 0.000218 | 0.000232 | 0.000187 | 0.000210 | 0.000200 | 0.000202 | 0.000224 | 0.000225 | 0.000246 | 0.000269 |
|    TimSort     | 0.000009 | 0.000008 | 0.000006 | 0.000009 | 0.000012 | 0.000014 | 0.000018 | 0.000020 | 0.000029 | 0.000026 | 0.000029 | 0.000033 | 0.000039 | 0.000042 | 0.000045 | 0.000047 |
|  TimSortCopy   | 0.000004 | 0.000004 | 0.000007 | 0.000009 | 0.000013 | 0.000018 | 0.000018 | 0.000021 | 0.000030 | 0.000026 | 0.000031 | 0.000036 | 0.000039 | 0.000045 | 0.000064 | 0.000061 |

![Array size 100 .. 1500](./pngs/100___1_500.png)
####
As we can see ```InsertionSort``` method is very slow, and even on 1500 elements execution time is > 100 msec. We can see a complexity $O(n^{2})$ from this graph.\
So, we will skip this method for the next tests with larger arrays.
All other algorithms are much faster, so it is hard to compare at this scale.

### Array size 10_000 .. 150_000
|  Sort method   |    0     |  10000   |  20000   |  30000   |  40000   |  50000   |  60000   |  70000   |  80000   |  90000   |  100000  |  110000  |  120000  |  130000  |  140000  |  150000  |
|----------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|   MergeSort    | 0.000011 | 0.025158 | 0.045047 | 0.072619 | 0.101518 | 0.136448 | 0.178129 | 0.172758 | 0.205663 | 0.229395 | 0.238453 | 0.262172 | 0.291832 | 0.309547 | 0.361195 | 0.389305 |
|   TimSorted    | 0.000009 | 0.002285 | 0.005258 | 0.009566 | 0.014338 | 0.017747 | 0.019155 | 0.024389 | 0.023476 | 0.026070 | 0.029772 | 0.038775 | 0.038237 | 0.040559 | 0.044209 | 0.049126 |
|    TimSort     | 0.000010 | 0.000373 | 0.000750 | 0.001180 | 0.001708 | 0.002278 | 0.003358 | 0.003231 | 0.003469 | 0.004001 | 0.004405 | 0.004888 | 0.005305 | 0.005984 | 0.006399 | 0.006877 |
|  TimSortCopy   | 0.000006 | 0.000363 | 0.000756 | 0.001178 | 0.001664 | 0.002051 | 0.002755 | 0.003012 | 0.003468 | 0.004044 | 0.004461 | 0.004906 | 0.005330 | 0.006135 | 0.006575 | 0.006929 |

![Array size 10_000 .. 150_000](./pngs/10_000___150_000.png)
####
Now we can see than the ```MergeSort``` algorithm is quite fast (150_000 elements ~400msec). We can see that the time complexity looks like $O(n\cdot log(n))$.\
But it is still far slower than embedded algorithms used by Python (it is expected even because the embedded algorithms are implemented on C/C++ inside an interpreter).\
Let's go further and compare ```sort()``` and ```sorted()```.

### Array size 100_000 .. 1_500_000
|  Sort method   |    0     |  100000  |  200000  |  300000  |  400000  |  500000  |  600000  |  700000  |  800000  |  900000  | 1000000  | 1100000  | 1200000  | 1300000  | 1400000  | 1500000  |
|----------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|   TimSorted    | 0.000016 | 0.043409 | 0.071077 | 0.129526 | 0.156312 | 0.212049 | 0.277375 | 0.312091 | 0.381342 | 0.435972 | 0.484519 | 0.541166 | 0.604219 | 0.655511 | 0.734962 | 0.773907 |
|    TimSort     | 0.000010 | 0.004501 | 0.009452 | 0.014848 | 0.019778 | 0.025554 | 0.030511 | 0.035615 | 0.039499 | 0.045089 | 0.051016 | 0.058156 | 0.063133 | 0.067140 | 0.070851 | 0.076061 |
|  TimSortCopy   | 0.000004 | 0.005149 | 0.010797 | 0.015282 | 0.020690 | 0.025655 | 0.030962 | 0.036438 | 0.040222 | 0.047118 | 0.051067 | 0.056087 | 0.064348 | 0.065206 | 0.071819 | 0.086923 |

![Array size 100_000 .. 1_500_000](./pngs/100_000___1_500_000.png)
####
At this step we got interesting results. Function ```sorted()``` is fast: 1_500_000 elements ~800 msec, but ```sort()``` is ~10 times faster.\
Even more: if we want to get a new list it is still ~10 faster to ```new_list = old_list.copy().sort()``` than ```new_list = sorted(old_list)```. It can be explained by a few facts:
 - ```sorted()``` - more generic function which can work with different types of iterable data not only a list
 - ```sort()``` - list-optimized method

## Conclusions
We can see that it is essential to have an optimized algorithm. Also, we have to understand and know the complexity (big-O) of an algorithm we are going to use or implement.\
As well, we can see that any algorithm written in Python will not be fast enough compared to an existing embedded or library algorithm, especially when it is implemented in C/C++.\
One additional result is that ```sorted()``` is much slower than ```sort()```. So we must consider using ```sort()``` anytime when possible.