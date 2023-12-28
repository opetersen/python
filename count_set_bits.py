#!/usr/bin/env python3

import timeit


def bit_counter_bit_count(num):
    return sum(i.bit_count() for i in range(num))


if __name__ == '__main__':
    num = 10000000
    start = timeit.default_timer()
    data = bit_counter_bit_count(num)
    end = timeit.default_timer()
    print(f"Time taken by bin method: {end - start} seconds")
    print(f"Number of set bits: {data}")
