"""
Репозиторий для работы с базой
"""

from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import PersonForm, create_person_form

from .models import Person


async def save_person(
    session: AsyncSession,
    person_form: PersonForm,
) -> Person:
    """
    Сохраняем форму в базу
    :param session: текущая сессия
    :param person_form: заполненная форма
    :return: пользователя, созданного в базе
    """
    person = Person(
        name=person_form.name,
        city=person_form.city,
    )

    session.add(person)
    await session.commit()
    await session.refresh(person)

    return person


async def get_person_list(session: AsyncSession) -> List[PersonForm]:
    """
    Получаем все анкеты из базы
    :param session: текущая сессия
    :return: список из заполненных форм
    """
    all_persons_query = select(Person)
    result = await session.execute(all_persons_query)
    persons = result.scalars().all()
    person_list = [create_person_form(person.name, person.city) for person in persons]
    return person_list
