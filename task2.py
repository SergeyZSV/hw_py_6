# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста).

# text = 'That is, until he tried to broker a deal selling access to the worlds most powerful satellite surveillance system to the highest bidder. When caught, Backman accepted prison as the one option that would keep him safe and alive, since the interested parties (the Israelis, the Saudis, the Russians, and the Chinese) were all itching to get their hands on his secrets at any cost. Little does he know that his own government has designs on accessing that information--or at least letting it die with him. Now, six years after his incarceration, the director of the CIA convinces a lame duck president to pardon Backman, and the broker becomes a free man--and an open target.'



def coun(text):
    c = 0
    for i in text:
        c += 1
    return c

init_text = 'decoded_text.txt'


def enc(directory: str) -> str:
    with open(directory, 'r') as file:
        text = file.read()
        text_convert = text + ' '
        list_code = []
        count = 1
        for i in range(0, len(text_convert) - 1):
            if text_convert[i] == text_convert[i + 1]:
                count += 1
            else:
                list_code.append((count, text_convert[i]))
                count = 1
        result_str = ''
        for el in list_code:
            result_str += f'{el[0]}{el[1]}'
    return result_str


def dec(directory: str) -> str:
    with open(directory, 'r') as file:
        text = file.read()
        result_str = ''
        for i in range(1, len(text)):
            if not text[i].isdigit():
                c = 0
                while c != int(text[i - 1]):
                    result_str += text[i]
                    c += 1
    return result_str


with open('encoded_text.txt', 'w') as file:
    file.write(enc(init_text))

print(enc(init_text))
print(dec('encoded_text.txt'))



