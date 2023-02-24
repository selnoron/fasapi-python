class Book:
    """Модель книги для нашего проекта."""

    def __init__(
        self,
        title: str,
        description: str,
        list_count: int,
        price: float,
        rate_list: list[int]
    ) -> None:
        self.title = title
        self.description = description
        self.list_count = list_count
        self.price = price 
        self.rate_list = rate_list

    @property
    def rate(self) -> float:
        return sum(self.rate_list) / len(self.rate_list)
    
    def save(self) -> None:
        jony: dict = {
            "title": self.title,
            "description": self.description,
            "list_count": self.list_count,
            "price": self.price,
            "rate_list": self.rate_list
        }
        return jony

    def delete() -> None:
        pass

    def update() -> None:
        pass
