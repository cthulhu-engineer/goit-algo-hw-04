import random


def generate_data(n):
    ordered_data = list(range(n))
    reverse_data = list(range(n, 0, -1))
    random_data = random.sample(range(n), n)

    return ordered_data, reverse_data, random_data
