#Дано неотрицательное целое число. Найдите число десятков в его десятичной записи (то есть вторую справа цифру его десятичной записи).


# adadi pesha megirad
number = int(input())

# adadi pusta megirad
tens_digit = (number // 10) % 10
# adadi bayna print 
print( tens_digit)