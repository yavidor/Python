from pip._vendor.distlib.compat import raw_input
import sys
import os

__author__ = "yavidor"


def divv(num1, num2):
    return float(num1) / float(num2)


def summer(x):
    y = x[0]
    for element in x[1::]:
        y = y + element
    print(y)


def bet():
    kelet = raw_input()
    if 'a' in kelet:
        kelet = kelet.replace('a', 'aba')
        print(kelet)
    if 'e' in kelet:
        kelet = kelet.replace('e', 'ebe')
        print(kelet)
    if 'i' in kelet:
        kelet = kelet.replace('i', 'ibi')
        print(kelet)
    if 'o' in kelet:
        kelet = kelet.replace('o', 'obo')
        print(kelet)
    if 'u' in kelet:
        kelet = kelet.replace('u', 'ubu')
        print(kelet)
    print(kelet.__eq__("abanibi obohebev obotabach"))
    return kelet


def main():
    bet()
    summer([10, 11, 12, 0.75])
    summer([True, False, True, True])
    summer(['aa', 'bb', 'cc'])
    summer([[1, 2, 3, 'a'], [4, 'b', 'c', 'd']])
    assert divv(9, 3) == 3, "oops"
    input_file = open(r'C:\Users\yonat\desktop\text.txt', 'r')
    output_file = open(r'C:\Users\yonat\desktop\txet.txt', 'w')
    output_file.write(input_file.read())
    a = open(sys.argv[1], 'r')
    print(a.read())
    try:
        print(os.listdir(sys.argv[2]))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
