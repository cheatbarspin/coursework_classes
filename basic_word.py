class BasicWord:
    # Инициализатор нужен, чтобы использовать и обращаться к заданным переменным
    # 1ым аргументом будет слово, 2ым список под-слов
    def __init__(self, word: str, correct_word: list):
        self.word = word
        self.correct_word = correct_word

    def word_check(self, user_answer) -> bool:
        """Проверка введенного слова в списке допустимых под-слов"""
        return user_answer in self.correct_word

    def word_counter(self) -> int:
        """Подсчет количества под-слов"""
        return len(self.correct_word)

    # нужен для показа объекта класса
    def __repr__(self):
        return f" {self.word} "
