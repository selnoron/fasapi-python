# fast api
import fastapi
import pydantic
# typing
import typing as t
# random
import names
import random


app = fastapi.FastAPI()
books: list['Book'] = []

class Book:
    """Модель книги для нашего проекта."""

    def __init__(
        self,
        id: int,
        title: str,
        description: str,
        list_count: int,
        price: float,
        rate_list: list[int]
    ) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.list_count = list_count
        self.price = price 
        self.rate_list = rate_list

    @property
    def rate(self) -> float:
        return sum(self.rate_list) / len(self.rate_list)
    
    @staticmethod
    def return_to_me(book: 'Book') -> dict:
        return {
            'id': book.id,
            'title': book.title,
            'description': book.description,
            'list_count': book.list_count,
            'price': book.price,
            'rate': book.rate
        }

for i in range(1000):
    book = Book(
        id=i,
        title=names.get_first_name(),
        description=names.get_last_name(),
        price=round(
            random.random() * 500 + 500,
            2
        ),
        list_count=random.randint(100, 600),
        rate_list=[
            random.randint(1, 10) 
            for _ in range(random.randint(1, 60))
        ]
    )
    books.append(Book.return_to_me(book))

@app.get('/books', response_model=t.Optional[list[dict]])
def get_all_books():
    return books

@app.get('/books/{bo_id}', response_model=t.Optional[dict])
def get_book(bo_id: int):
    return [i for i in books if i.get('id') == bo_id][0]
