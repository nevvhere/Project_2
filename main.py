import random

# Import the movie and series lists from another file
from movies_series import movies
from movies_series import series

def get_random_movie(genre, watched_movies):
  """Selects a random movie from the list, excluding watched movies."""
  available_movies = [movie for movie in movies[genre] if movie not in watched_movies]
  if available_movies:
    return random.choice(available_movies)
  else:
    return "Вы посмотрели все фильмы этого жанра"

def get_random_series(genre, watched_series):
  """Selects a random series from the list, excluding watched series."""
  available_series = [serie for serie in series[genre] if serie not in watched_series]
  if available_series:
    return random.choice(available_series)
  else:
    return "Вы посмотрели все сериалы этого жанра"

def main():
  """Main function for the program."""
  watched_movies = []
  watched_series = []

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

      random_movie = get_random_movie(genre, watched_movies)
      if random_movie != "Вы посмотрели все фильмы этого жанра":
        print(f"\nРандомный фильм: {random_movie}\n")
        watched_movies.append(random_movie)
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

      random_series = get_random_series(genre, watched_series)
      if random_series != "Вы посмотрели все сериалы этого жанра":
        print(f"\nРандомный сериал: {random_series}\n")
        watched_series.append(random_series)
      else:
        print(random_series)

    elif choice == "3":
      print("\nПросмотренные фильмы: ")
      if watched_movies:
        for movie in watched_movies:
          print(movie)
      else:
        print("Сначала надо посмотреть фильм:)")

    elif choice == "4":
      print("\nПросмотренные сериалы: ")
      if watched_series:
        for serie in watched_series:
          print(serie)
      else:
        print("Сначала надо посмотреть сериал:)")

    elif choice == "5":
      break
    else:
      print("Нет такого выбора:(")

if __name__ == "__main__":
  main()
