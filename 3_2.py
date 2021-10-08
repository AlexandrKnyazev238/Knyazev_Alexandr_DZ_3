# Task_2

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


def num_translate_adv(eng_word):
    if eng_word[0] == eng_word[0].upper():
        eng_word = eng_word.lower()
        return eng_rus_dict[eng_word].title()
    else:
        return eng_rus_dict[eng_word]


print(num_translate_adv('One'))
print(num_translate_adv('two'))
print(num_translate_adv(input('Введите число от 0 "Zero" до 10 "ten": ')))
