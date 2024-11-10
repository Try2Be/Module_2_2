first = input('Введите первое число : ')
second = input('Введите второе число : ')
third = input('Введите третье число : ')
if first.isdigit() and second.isdigit() and third.isdigit():
    first = int(first)
    second = int(second)
    third = int(third)
    if first == second == third:
        print ('(3)')
    elif first == second or first == third or second == third:
        print ('(2)')
    else:
        print ('0')
else:
    print ('Ошибка: Введите челые числа!')