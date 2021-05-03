from random import randint
from timeit import repeat


def sorting_time(algorithm, array):
        code = f"from davidminilab2 import {algorithm}" \
            if algorithm != "sorted" else ""

        stmt = f"{algorithm}({array})"
        times = repeat(setup=code, stmt=stmt, repeat=3, number=10)
        print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def bubble_sort(sort_list):
    complete = False
    rounds = 0
    table_values = [list(sort_list)]
    while not complete:
        complete = True
        for value in range(len(sort_list)-1):
            if sort_list[value] > sort_list[value+1]:
                sort_list[value], sort_list[value+1] = sort_list[value+1], sort_list[value]
                complete = False
        if not complete: table_values.append(list(sort_list))
        rounds += 1
    print(table_values)
    return table_values, rounds

def bubble_sort_characters(sort_list):
    complete = False
    rounds = 0
    table_values = [list(sort_list)]
    while not complete:
        complete = True
        for value in range(len(sort_list)-1):
            if ord(sort_list[value]) > ord(sort_list[value+1]):
                sort_list[value], sort_list[value+1] = sort_list[value+1], sort_list[value]
                complete = False
        if not complete: table_values.append(list(sort_list))
        rounds += 1
    print(table_values)
    return table_values, rounds

if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(8)]
    print(array)
    print(sorting_time("sorted", array))
    sort_list, rounds = bubble_sort(array)
    print(f"The list {sort_list} was sorted in {rounds} rounds.")
