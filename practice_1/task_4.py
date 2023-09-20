# -*- coding: utf-8 -*-
"""
Разработайте программу, запрашивающую у  пользователя целое четырехзначное число и подсчитывающую сумму составляющих его цифр. Например, если пользователь введет число 3141,
 программа должна вывести 
следующий результат: 3 + 1 + 4 + 1 = 9

@author: Savant
"""


def digits(num: int, *, base: int = 10):
    num = int(str(num)[::-1])
    while num > 0:
        num, mod = divmod(num, base)
        yield mod


def main():
    while True:
        text = input("Enter a 4-digit number: ")

        try:
            num = int(text)
        except ValueError:
            print("Error: not a number!")
            continue

        if not (1000 <= num <= 9999):
            print("Error: not a 4-digit number!")
            continue

        break

    num_digits = list(digits(num))
    message = f"{' + '.join(str(d) for d in num_digits)} = {sum(num_digits)}"

    print(message)


if __name__ == "__main__":
    main()
