import random
from movies import movies
from series import series
from exceptions import InvalidGenreError

class EntertainmentPicker:
    def __init__(self):
        self.watched_movies = []
        self.watched_series = []

    def get_random_movie(self, genre):
        """выбирает рандомный фильм из списка, исключая просмотренные"""
        if genre not in movies:
            raise InvalidGenreError(f"Genre '{genre}' not found")
        available_movies = [movie for movie in movies[genre] if movie not in self.watched_movies]
        if available_movies:
            return random.choice(available_movies)
        else:
            return "Вы посмотрели все фильмы этого жанра"

    def get_random_series(self, genre):
        """выбирает рандомный сериал из списка, исключая просмотренне"""
        if genre not in series:
            raise InvalidGenreError(f"Genre '{genre}' not found")
        available_series = [serie for serie in series[genre] if serie not in self.watched_series]
        if available_series:
            return random.choice(available_series)
        else:
            return "Вы посмотрели все сериалы этого жанра"

    def show_watched_movies(self):
        """печатает лист просмотренных фильмов"""
        if self.watched_movies:
            print("Просмотренные фильмы:")
            for movie in self.watched_movies:
                print(movie)
        else:
            print("Сначала надо посмотреть фильм:)")

    def show_watched_series(self):
        """печатает лист просмотреннх сериалов"""
        if self.watched_series:
            print("Просмотренные сериалы:")
            for serie in self.watched_series:
                print(serie)
        else:
            print("Сначала надо посмотреть сериал:)")

def main():
    picker = EntertainmentPicker()
    while True:
        print("\nВыберите действие:")
        print("1. Рандомный фильм")
        print("2. Рандомный сериал")
        print("3. Просмотренные фильмы")
        print("4. Просмотренные сериалы")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            print("\nВыберите жанр:")
            print("1. Драма")
            print("2. Комедия")
            print("3. Хоррор / Триллер")

            genre_choice = input("Введите ваш выбор: ")

            if genre_choice == "1":
                genre = "Драма"
            elif genre_choice == "2":
                genre = "Комедия"
            elif genre_choice == "3":
                genre = "Хоррор / Триллер"
            else:
                print("Такого жанра нет:(")
                continue

            try:
                random_movie = picker.get_random_movie(genre)
            except InvalidGenreError as e:
                print(f"Ошибка: {e}")
                continue
            if random_movie != "Вы посмотрели все фильмы этого жанра":
                print(f"\nРандомный фильм: {random_movie}\n")
                picker.watched_movies.append(random_movie)
            else:
                print(random_movie)

        elif choice == "2":
            print("\nВыберите жанр: ")
            print("1. Драма")
            print("2. Комедия")
            print("3. Хоррор / Триллер")

            genre_choice = input("Введите ваш выбор: ")

            if genre_choice == "1":
                genre = "Драма"
            elif genre_choice == "2":
                genre = "Комедия"
            elif genre_choice == "3":
                genre = "Хоррор / Триллер"
            else:
                print("Такого жанра нет:(")
                continue

            try:
                random_series = picker.get_random_series(genre)
            except InvalidGenreError as e:
                print(f"Ошибка: {e}")
                continue

            if random_series != "Вы посмотрели все сериалы этого жанра":
                print(f"\nРандомный сериал: {random_series}\n")
                picker.watched_series.append(random_series)
            else:
                print(random_series)

        elif choice == "3":
            picker.show_watched_movies()

        elif choice == "4":
            picker.show_watched_series()

        elif choice == "5":
            break
        else:
            print("Нет такого выбора:(")

if __name__ == "__main__":
    main()
