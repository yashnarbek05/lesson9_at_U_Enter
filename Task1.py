import random

def lottery():
    set1 = set()

    while True:
        if len(set1) != 6:
            set1.add(random.randint(1, 50))
        else:
            break
    return sorted(set1)


if __name__ == '__main__':
    print(lottery())
