#Дано трехзначное число. Найдите сумму его цифр.

number = int(input())


sum_of_digits = sum(int(digit) for digit in str(number))

print(sum_of_digits)