# Task_1

eng_rus_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(eng_word):
    return eng_rus_dict.get(eng_word)


print(num_translate('one'))
print(num_translate('eight'))
print(num_translate(input('Введите число от 0 "zero" до 10 "ten": ')))
