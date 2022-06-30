# Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;


to_solve = '305+729-321*1000/5/6/7'


def calc(text: str):
    new_text = ''
    for i in range(0, len(text)):
        if text[i].isdigit():
            new_text += text[i]
        else:
            new_text += ' ' + text[i] + ' '
    list_to_solve = new_text.split(' ')
    for el in list_to_solve:        # конвертируем численные элементы списка в int
        if el.isdigit():
            list_to_solve[list_to_solve.index(el)] = int(el)
    operations = 0      # количество математических операций в строке
    for el in list_to_solve:
        if type(el) == str:
            operations += 1
    count = 0
    while count != operations:
        i = 0
        while i < len(list_to_solve):

            if list_to_solve.count('*') > 0 or list_to_solve.count('/') > 0:
                j = 0
                while j < len(list_to_solve):
                    if list_to_solve[j] == '*':
                        new_element = list_to_solve[j - 1] * list_to_solve[j + 1]
                        list_to_solve.insert(j - 1, new_element)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                        j = 0
                    elif list_to_solve[j] == '/':
                        new_element = int(list_to_solve[j - 1]) / int(list_to_solve[j + 1])
                        list_to_solve.insert(j - 1, new_element)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                        j = 0
                    else:
                        j += 1
                i = 0

            elif list_to_solve.count('+') > 0 or list_to_solve.count('-') > 0:
                j = 0
                while j < len(list_to_solve):
                    if list_to_solve[j] == '+':
                        new_element = list_to_solve[j - 1] + list_to_solve[j + 1]
                        list_to_solve.insert(j - 1, new_element)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                        j = 0
                    elif list_to_solve[j] == '-':
                        new_element = list_to_solve[j - 1] - list_to_solve[j + 1]
                        list_to_solve.insert(j - 1, new_element)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                        list_to_solve.pop(j)
                        j = 0
                    else:
                        j += 1
                i = 0
            i += 1
        count += 1
    result = list_to_solve[0]
    return result


print(f'{to_solve} = {calc(to_solve)}')
