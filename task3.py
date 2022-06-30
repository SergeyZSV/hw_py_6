# ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . Если в строку включены числа или специальные символы, они должны быть возвращены как есть. Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений).
# Не использовать функцию encode.

alph_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def rot13_enc(text: str, alph=alph_ru) -> str:
    result_str = ''
    text = text.lower()
    for i in range(0, len(text)):
        if not text[i].isalpha():
            result_str += text[i]
        else:
            result_str += alph[(alph.index(text[i]) + 13) % len(alph)]
    return result_str


def rot13_dec(text: str, alph=alph_ru) -> str:
    result_str = ''
    text = text.lower()
    for i in range(0, len(text)):
        if not text[i].isalpha():
            result_str += text[i]
        else:
            result_str += alph[(alph.index(text[i]) - 13) % len(alph)]
    return result_str


print(rot13_dec(rot13_enc('Например, число 12')))
