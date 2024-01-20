import timeit

from data_generator import generate_data
from insertion_sort import insertion_sort
from merge_sort import merge_sort


def test_sorting_algorithm(algorithm, data):
    return timeit.timeit(lambda: algorithm(data[:]), number=1)


def perform_tests(n):
    ordered_data, reverse_data, random_data = generate_data(n)

    for sort_alg in [insertion_sort, merge_sort, sorted]:
        for data, data_type in zip([ordered_data, reverse_data, random_data],
                                   ["Ordered", "Reverse", "Random"]):
            time = test_sorting_algorithm(sort_alg, data)
            print(f"{sort_alg.__name__} on {data_type} data: {time} seconds")


n = 10000
perform_tests(n)
