import random


def count_range(numbers, minn, maxx):
    return sum(minn <= num < maxx for num in numbers)


    return count

if __name__ == '__main__':
    print(count_range([21,212,4124,1], 1, 210))
