
import numpy as np
import random


def generate_random_number_array(size, max_value=100, decimals=2):
    array = np.ones(size) * max_value
    for i in range(size):
        array[i] *= random.random()
        array[i] = round_to(array[i], decimals)
    return array


def round_to(value, decimals):
    value *= 10 ** decimals
    value = round(value)
    value /= 10 ** decimals
    return value