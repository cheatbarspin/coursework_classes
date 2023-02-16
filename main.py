# Импорт класса Player и функции load_json,
# первый класс не нужен ибо он уже используется в функции
from players import Player
from utils import load_json

# Просим ввод от пользователя и инициализируем класс Player
player_name = input("Введите ваше имя")
player = Player(player_name)
print(f"Привет {player}")

# Достаем наш случайный словарь из слова и его под-слов,
# чтобы после итерироваться
random_word = load_json()
print(f"Составьте {random_word.word_counter()} слов из слова {random_word}")
print(f"Слова должны быть не короче 3 букв\nчтобы закончить игру, угадайте все слова или напишите stop")

# Используем цикл while, чтобы пока не выполнятся все условия
# и кол-во отвеченных слов не будет равным кол-ву данных слов
while player.using_words_count() != random_word.word_counter():
    user_answer = input()
    if len(user_answer) < 3:
        print("слишком короткое слово")
        continue
    if user_answer == 'stop':
        break
    if random_word.word_check(user_answer):
        if player.check_before(user_answer):
            print("это слово уже использовано")
        else:
            player.using_words_list(user_answer)
            print("Верно")
    else:
        print("Такого слова нет")

print(f"Игра завершена, вы угадали {player.using_words_count()} слов!")


