import random


def isSorted(numbers):

    if len(numbers) <= 2:
        return True

    escending = numbers[0] < numbers[1];

    for i in range(0, len(numbers) - 1):
        if escending and numbers[i] > numbers[i + 1]:
            return False
        elif not escending and numbers[i] < numbers[i + 1]:
            return False

    return True

if __name__ == '__main__':
    str = input("enter numbers separeted with space: ")

    numbers = list(map(int, str.split()))

    print(isSorted(numbers))
