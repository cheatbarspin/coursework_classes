from basic_word import BasicWord
import json, random


# Читаем файл, форматируем в питон, достаем случайный словарь из списка
# и инициализируем класс
def load_json():
    with open('dict.json', 'r') as file:
        our_list = json.load(file)
        rnd_word = random.choice(our_list)
        return BasicWord(rnd_word['word'], rnd_word['subwords'])
