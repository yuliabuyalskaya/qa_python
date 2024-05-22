import pytest
from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2


    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_books_genre_is_null(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre[name] == ''

    def test_set_book_genre_right_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключение Васи Куролесова')
        collector.set_book_genre('Приключение Васи Куролесова', 'Комедии')
        assert collector.books_genre['Приключение Васи Куролесова'] == 'Комедии'


    def test_get_book_genre_right_book(self):
        collector = BooksCollector()
        collector.add_new_book('Приключение Васи Куролесова')
        collector.set_book_genre('Приключение Васи Куролесова', 'Комедии')
        assert collector.get_book_genre('Приключение Васи Куролесова') == 'Комедии'


    def test_get_books_with_specific_genre_two_books_with_rigt_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключение Васи Куролесова')
        collector.add_new_book('12 стульев')
        collector.set_book_genre('Приключение Васи Куролесова', 'Комедии')
        collector.set_book_genre('12 стульев', 'Комедии')
        assert len(collector.get_books_with_specific_genre('Комедии')) == 2

    def test_get_books_genre_type_result_is_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Приключение Васи Куролесова')
        collector.add_new_book('12 стульев')
        collector.set_book_genre('Приключение Васи Куролесова', 'Комедии')
        collector.set_book_genre('12 стульев', 'Комедии')
        assert type(collector.get_books_genre()) == dict



    @pytest.mark.parametrize('name, genre', [['Оно', 'Ужасы'], ['Убийство', 'Детективы']])
    def test_get_books_for_children_age_rating_books_not_in_result(self, name, genre):
        collector  = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        result = collector.get_books_for_children()
        assert len(collector.get_books_for_children()) == 0


    @pytest.mark.parametrize('name', ['Оно', '12 стульев'])
    def test_add_book_in_favorites_add_new_favorite_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites


    @pytest.mark.parametrize('name', ['Оно', '12 стульев'])
    def test_delete_book_from_favorites_right_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    def test_get_list_of_favorites_books_result_is_list(self):
        collector = BooksCollector()
        assert type(collector.favorites) == list





