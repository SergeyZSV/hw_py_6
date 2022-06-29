# Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;


to_solve = '1-2*3'


def calc(text: str):
    list_to_solve = []
    for el in text:
        list_to_solve.append(el)
    for el in list_to_solve:
        if el.isdigit():
            list_to_solve[list_to_solve.index(el)] = int(el)
    operations = 0      # количество математических операций в строке
    for el in list_to_solve:
        if type(el) == str:
            operations += 1
    count = 0
    while count != operations:
        for i in range(0, len(list_to_solve) - 1):
            if list_to_solve.count('*') > 0:
                for j in range(0, len(list_to_solve) - 1):
                    if list_to_solve[j] == '*':
                        new_element = list_to_solve[j - 1] * list_to_solve[j + 1]
                        list_to_solve.insert(j - 1, new_element)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                break
            elif list_to_solve.count('/') > 0:
                for j in range(0, len(list_to_solve) - 1):
                    if list_to_solve[j] == '/':
                        new_element = list_to_solve[j - 1] / list_to_solve[j + 1]
                        list_to_solve.insert(j - 1, new_element)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                break
            if list_to_solve.count('+') > 0:
                for j in range(0, len(list_to_solve) - 1):
                    if list_to_solve[j] == '+':
                        new_element = list_to_solve[j - 1] + list_to_solve[j + 1]
                        list_to_solve.insert(j - 1, new_element)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                break
            if list_to_solve.count('-') > 0:
                for j in range(0, len(list_to_solve) - 1):
                    if list_to_solve[j] == '-':
                        new_element = list_to_solve[j - 1] - list_to_solve[j + 1]
                        list_to_solve.insert(j - 1, new_element)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                break
        count += 1
    result = list_to_solve[0]
    return result


print(f'{to_solve} = {calc(to_solve)}')
