import re


def main():
    str = '1,100人256人中'
    num = int(re.search(r'^\d+', re.sub(',', '', str)).group(0))
    # list = [int(s) for s in str.split() if s.isdigit()]
    print(num, type(num))


if __name__ == '__main__':
    main()
