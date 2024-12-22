import random
from movies import movies # Импорт словаря с жанрами фильмов
from series import series # Импорт словаря с жанрами сериалов
from exceptions import InvalidGenreError # Импорт пользовательского исключения

"""Создаются списки для хранения просмотренных фильмов и сериалов"""
class EntertainmentPicker:
    def __init__(self):
        self.watched_movies = [] # Список просмотренных фильмов
        self.watched_series = [] # Список просмотренных сериалов

 """выбирает рандомный фильм из списка, исключая просмотренные"""
    def get_random_movie(self, genre):
        if genre not in movies: # Проверка наличия жанра в словаре фильмов
            raise InvalidGenreError(f"Genre '{genre}' not found") 
        available_movies = [movie for movie in movies[genre] if movie not in self.watched_movies]
        if available_movies: # Возвращает случайный фильм
            return random.choice(available_movies)
        else: 
            return "Вы посмотрели все фильмы этого жанра"

"""выбирает рандомный сериал из списка, исключая просмотренне"""
    def get_random_series(self, genre):
        if genre not in series: # Проверка наличия жанра в словаре сериалов
            raise InvalidGenreError(f"Genre '{genre}' not found")
        available_series = [serie for serie in series[genre] if serie not in self.watched_series]
        if available_series:
            return random.choice(available_series) # Возвращает случайный сериал
        else:
            return "Вы посмотрели все сериалы этого жанра"

"""печатает лист просмотренных фильмов"""
    def show_watched_movies(self): # Проверяет не пуст ли список просмотренных фильмов
        if self.watched_movies: # Если нет, то выводит список просмотренных фильмов
            print("Просмотренные фильмы:")
            for movie in self.watched_movies:
                print(movie)
        else:
            print("Сначала надо посмотреть фильм:)") # Если список пуст, то выводит "Сначала надо посмотреть фильм:)"

 """печатает лист просмотреннх сериалов"""
    def show_watched_series(self): # Проверяет не пуст ли список просмотренных сериалов
        if self.watched_series: # Если нет, то выводит список просмотренных сериалов
            print("Просмотренные сериалы:")
            for serie in self.watched_series:
                print(serie)
        else:
            print("Сначала надо посмотреть сериал:)") # Если список пуст, то выводит "Сначала надо посмотреть сериалы:)"


"""Выбор действия через меню"""
def main():
    picker = EntertainmentPicker() # Создание объекта класса
    while True:
        print("\nВыберите действие:")
        print("1. Рандомный фильм")
        print("2. Рандомный сериал")
        print("3. Просмотренные фильмы")
        print("4. Просмотренные сериалы")
        print("5. Выйти")

        choice = input("Введите номер действия: ") # Ввод выбора пользователя

        if choice == "1": # Выбор случайного фильм
            print("\nВыберите жанр:")
            print("1. Драма")
            print("2. Комедия")
            print("3. Хоррор / Триллер")

            genre_choice = input("Введите ваш выбор: ") # Ввод жанра

            if genre_choice == "1":
                genre = "Драма"
            elif genre_choice == "2":
                genre = "Комедия"
            elif genre_choice == "3":
                genre = "Хоррор / Триллер"
            else:
                print("Такого жанра нет:(")
                continue # Возврат к началу цикла

            try:
                random_movie = picker.get_random_movie(genre) # Получение случайного фильма
            except InvalidGenreError as e:
                print(f"Ошибка: {e}")
                continue # Возврат к началу цикла
            if random_movie != "Вы посмотрели все фильмы этого жанра":
                print(f"\nРандомный фильм: {random_movie}\n")
                picker.watched_movies.append(random_movie) # Добавление фильма в просмотренные
            else:
                print(random_movie)

        elif choice == "2": # Выбор случайного сериала
            print("\nВыберите жанр: ")
            print("1. Драма")
            print("2. Комедия")
            print("3. Хоррор / Триллер")

            genre_choice = input("Введите ваш выбор: ") # Ввод жанра

            if genre_choice == "1":
                genre = "Драма"
            elif genre_choice == "2":
                genre = "Комедия"
            elif genre_choice == "3":
                genre = "Хоррор / Триллер"
            else:
                print("Такого жанра нет:(")
                continue # Возврат к началу цикла

            try:
                random_series = picker.get_random_series(genre) # Получение случайного сериала
            except InvalidGenreError as e:
                print(f"Ошибка: {e}")
                continue

            if random_series != "Вы посмотрели все сериалы этого жанра":
                print(f"\nРандомный сериал: {random_series}\n")
                picker.watched_series.append(random_series) # Добавление сериала в просмотренные
            else:
                print(random_series)

        elif choice == "3": # Вывод просмотренных фильмов
            picker.show_watched_movies()

        elif choice == "4": # Вывод просмотренных сериалов
            picker.show_watched_series()

        elif choice == "5": # Выход из программы
            break
        else:
            print("Нет такого выбора:(") # Если введено некорректное значение

if __name__ == "__main__":
    main() 
