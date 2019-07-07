import random


def main():
    num_list = list(range(1, 10))
    random.shuffle(num_list)

    for num in num_list:
        print(num)


if __name__ == '__main__':
    main()
