# qa_python
***
1) Уже написанный тест для примера (добавление 2 книг с помощью метода add_new_book)
2) test_add_new_book_books_genre_is_null - проверяет метод add_new_book - жанр добавленной книги в словаре -пустая строка
3) test_set_book_genre_right_genre - проверяет метод set_book_genre- добавляет жанр книги в словарь, по ключу - названию книги, при условии что жанр есть в списке жанров (атрибуте класса)
4) test_get_book_genre_right_book - проверяет метод get_book_genre, получение жанра книги по названию
5) test_get_books_with_specific_genre_two_books_with_rigt_genre - проверяет работу метода get_books_with_specific_genre с корректными данными (2 книги по 1 жанру), в результате которого мы получаем список книг по указанному жанру
6) test_get_books_genre_type_result_is_dict - проверяет метод get_books_genre - правильный формат данных (словарь) - сам атрибут проверяется в других тестах
7) test_get_books_for_children_age_rating_books_not_in_result - проверяет метод get_books_for_children (жанр ужасы и детективы не влючается в список книг для детей)
8) test_add_book_in_favorites_add_new_favorite_book - проверяет метод add_book_in_favorites, добавление книги по названию
9) test_delete_book_from_favorites_right_book - проверяет метод delete_book_from_favorites,удаление из избранного
10) test_get_list_of_favorites_books_result_is_list - проверяет что атрибук favorites возвращается списком


***