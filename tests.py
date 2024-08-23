from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # пример теста:
    # тестируем метод add_new_book_, добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две книги
        assert len(collector.get_books_genre()) == 2

    # Проверяем добавление книги с пустым названием
    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')  # Пытаемся добавить книгу с пустым названием
        # Проверяем, что книга не добавилась
        assert len(collector.get_books_genre()) == 0

    # Проверяем добавление книги с максимальной допустимой длиной названия
    def test_add_new_book_max_length(self):
        collector = BooksCollector()
        long_name = "Тайны глубин: Исчезновение Атлантиды и её секреты"
        collector.add_new_book(long_name)
        # Проверяем, что книга добавилась
        assert len(collector.get_books_genre()) == 1
        assert long_name in collector.get_books_genre()

    # Проверяем добавление книги с минимальной длиной названия
    def test_add_new_book_min_length(self):
        collector = BooksCollector()
        collector.add_new_book('X')  # Добавляем книгу с названием из одного символа
        # Проверяем, что книга добавилась
        assert len(collector.get_books_genre()) == 1
        assert 'X' in collector.get_books_genre()

    # Проверяем, что одну и ту же книгу нельзя добавить дважды
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Мастер и Маргарита')  # Пытаемся добавить книгу второй раз
        # Проверяем, что в словаре только одна такая книга
        assert len(collector.get_books_genre()) == 1

    # Проверяем установку жанра для существующей книги
    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')  # Устанавливаем жанр
        # Проверяем, что жанр установлен правильно
        assert collector.get_book_genre('1984') == 'Фантастика'

    # Проверяем, что установка несуществующего жанра не меняет жанр книги
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Неизвестный жанр')  # Пытаемся установить несуществующий жанр
        # Жанр книги должен остаться пустым
        assert collector.get_book_genre('1984') == ''

    # Проверяем, что установка жанра для несуществующей книги ничего не изменяет
    def test_set_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Неизвестная книга', 'Фантастика')  # Пытаемся установить жанр для несуществующей книги
        # Жанр для несуществующей книги не должен устанавливаться
        assert collector.get_book_genre('Неизвестная книга') is None

    # Проверяем, что возвращаются только книги с указанным жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('Сон в летнюю ночь')
        collector.set_book_genre('1984', 'Фантастика')
        collector.set_book_genre('Сон в летнюю ночь', 'Комедии')
        # Получаем книги с жанром 'Фантастика'
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert '1984' in fantasy_books
        assert 'Сон в летнюю ночь' not in fantasy_books

    # Проверяем, что возвращаются книги, подходящие детям
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Маленький принц', 'Мультфильмы')
        collector.set_book_genre('Сияние', 'Ужасы')
        # Книги без возрастного рейтинга (в данном случае только 'Маленький принц') должны вернуться
        books_for_children = collector.get_books_for_children()
        assert 'Маленький принц' in books_for_children
        assert 'Сияние' not in books_for_children

    # Проверяем добавление книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')  # Добавляем книгу в избранное
        # Проверяем, что книга добавлена в избранное
        assert '1984' in collector.get_list_of_favorites_books()

    # Проверяем удаление книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')  # Удаляем книгу из избранного
        # Проверяем, что книга удалена из избранного
        assert '1984' not in collector.get_list_of_favorites_books()

    # Проверяем получение списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')  # Добавляем книгу в избранное
        # Проверяем, что список избранных книг содержит добавленную книгу
        assert collector.get_list_of_favorites_books() == ['1984']

    # Проверяем правильность возвращаемого словаря с жанрами книг
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('Сияние')
        collector.set_book_genre('1984', 'Фантастика')
        # Проверяем, что словарь содержит корректные пары книга-жанр
        expected_genre_dict = {'1984': 'Фантастика', 'Сияние': ''}
        assert collector.get_books_genre() == expected_genre_dict

    # Проверяем добавление книги с длинным названием
    def test_add_new_book_with_long_name(self):
        collector = BooksCollector()
        long_name = "Приключения на краю Вселенной: Галактические войны"
        collector.add_new_book(long_name)
        # Проверяем, что книга с длинным названием добавлена
        assert len(collector.get_books_genre()) == 1
        assert long_name in collector.get_books_genre()
