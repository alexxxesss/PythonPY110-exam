import json
import random

from typing import Iterator
from faker import Faker
from conf import MODEL

fake_ru = Faker(locale="ru_RU")


def main():
    num_books = int(input("Введите количество книг, которое нужно сгенерировать: "))
    serial_num = int(input("Введите порядковый номер, с которого начинать: "))
    list_books = []
    books_gen = books(serial_num)
    for i in range(num_books):
        list_books.append(next(books_gen))
    with open("output.txt", "w", encoding="utf-8") as f:
        json.dump(list_books, f, ensure_ascii=False, indent=4)


def books(count: int = 1) -> Iterator[dict]:
    """
    Функция генератор формирмирует словарь со значениями: "MODEL", порядковое число, информация о книге
    :param count: начальное порядковое значение
    :return: генерирует словарь
    """
    while True:

        book = {
            "model": MODEL,
            "pk": count,
            "fields": fields()
        }
        count += 1
        yield book


def fields() -> dict:
    """
    Функция генерирует словарь, в котором содержится информация о книге
    :return: возвращает словарь с наименованием книги и другой информацией
    """
    fields_dict = {
        "title": name_books(),
        "year": release_date(),
        "pages": pages_gen(),
        "isbn13": isbn13_gen(),
        "rating": rating_gen(),
        "price": price_gen(),
        "author": author_gen()
    }
    return fields_dict


def name_books() -> str:
    """
    Функция считывает файл со списком книг
    :return: возвращает список книг
    """
    with open("books.txt", "r", encoding="utf-8") as file:
        books_list = [i for i in file.read().split("\n")]
    return random.choice(books_list)


def release_date(min_year: int = 1700, max_year: int = 2021) -> int:
    """
    Функция гененрирует случайное значение года в промежутке 1700 - 2021г
    :param min_year: 1700г
    :param max_year: 2021г
    :return: возвращает год
    """
    return random.randint(min_year, max_year)


def pages_gen(max_pages: int = 2500) -> int:
    """
    Функция гененрирует случайное кол-во страниц в книге от 0 до 2500
    :param max_pages: 2021г
    :return: возвращает кол-во страниц
    """
    return random.randint(0, max_pages)


def isbn13_gen() -> str:
    """
    Функция гененрирует случайное значение isbn13
    :return: возвращает isbn13
    """
    return fake_ru.isbn13()


def rating_gen(min_rate: int = 0, max_rate: int = 5) -> float:
    """
    Функция гененрирует случайный рейтинг книги в промежутке от 0.00 до 5.00
    :param min_rate: 0.00
    :param max_rate: 5.00
    :return: возвращает рейтинг книги
    Результат округляется до 2х значений после запятой
    """
    return round(random.uniform(min_rate, max_rate), 2)


def price_gen(min_price: int = 0, max_price: int = 2000) -> float:
    """
    Функция гененрирует случайную стоимость книги в промежутке от 0.00 руб до 2000.00 руб
    :param min_price: 0.00 руб
    :param max_price: 2000.00 руб
    :return: возвращает стоимосоть книги
    Результат округляется до 2х значений после запятой
    """
    return round(random.uniform(min_price, max_price), 2)


def author_gen() -> list:
    """
    Функция гененрирует список авторов книги в количестве от 1 до 3
    :return: возвращаяет список в виде строки
    """
    num_authors = random.randint(1, 3)
    names_list = [fake_ru.name() for _ in range(num_authors)]
    return names_list


if __name__ == "__main__":
    main()
