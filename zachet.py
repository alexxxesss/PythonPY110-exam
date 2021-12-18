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
    while True:
        book = {
            "model": MODEL,
            "pk": count,
            "fields": fields()
        }
        count += 1
        yield book


def fields() -> dict:
    fields_dict = {
    "title": name_books(),
    "year": release_date(),
    "pages": pages_gen(),
    "isbn13": isbn13_gen(),
    "rating":rating_gen(),
    "price": price_gen(),
    "author": author_gen()
    }
    return fields_dict


def name_books() -> str:
    with open("books.txt", "r", encoding="utf-8") as file:
        books_list = [i for i in file.read().split("\n")]
    return random.choice(books_list)


def release_date() -> int:
    return random.randint(1700, 2021)


def pages_gen(max_pages: int = 2500) -> int:
    return random.randint(0, max_pages)


def isbn13_gen() -> str:
    return fake_ru.isbn13()


def rating_gen(min_rate: int = 0, max_rate: int = 5) -> float:
    return round(random.uniform(min_rate, max_rate),2)


def price_gen(min_price: int = 0, max_price: int = 2000) -> float:
    return round(random.uniform(min_price, max_price),2)


def author_gen() -> list:
    num_authors = random.randint(1, 3)
    names_list = [fake_ru.name() for _ in range(num_authors)]
    return names_list


if __name__ == "__main__":
    main()