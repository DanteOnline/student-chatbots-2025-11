from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Person
from app.models import PersonForm, create_person_form


async def save_person(
    session: AsyncSession,
    person_form: PersonForm,
) -> Person:
    person = Person(
        name=person_form.name,
        city=person_form.city,
    )

    session.add(person)
    await session.commit()
    await session.refresh(person)

    return person


async def get_person_list(session: AsyncSession) -> List[PersonForm]:
    all_persons_query = select(Person)
    result = await session.execute(all_persons_query)
    persons = result.scalars().all()
    person_list = [
        create_person_form(person.name, person.city) for person in persons
    ]
    return person_list
