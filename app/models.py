"""
Main models
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class PersonForm:
    """
    Данные пользователя
    """
    name: str
    city: str

    def __str__(self):
        return f'{self.name} из {self.city}'


def create_person_form(name: str, city: str) -> PersonForm:
    """
    Создание данных пользователя
    """
    return PersonForm(name=name, city=city)
