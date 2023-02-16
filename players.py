
class Player:
    # Аргументом будет имя пользователя
    def __init__(self, user_name: str):
        self.user_name = user_name
        self.using_words = []

    def using_words_count(self) -> int:
        """Получение количества использованных слов"""
        return len(self.using_words)

    def using_words_list(self, user_answer):
        """Добавление слова в использованные слова"""
        self.using_words.append(user_answer)

    def check_before(self, user_answer) -> bool:
        """Проверка использования данного слова до этого"""
        return user_answer in self.using_words

    def __repr__(self):
        return f"{self.user_name}"

