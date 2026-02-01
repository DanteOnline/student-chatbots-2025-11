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
    tg_id: int

    def __str__(self):
        return f'{self.name} из {self.city}'


def create_person_form(name: str, city: str, tg_id: int) -> PersonForm:
    """
    Создание данных пользователя
    """
    return PersonForm(name=name, city=city, tg_id=tg_id)
