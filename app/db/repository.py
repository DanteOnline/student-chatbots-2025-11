from sqlalchemy.ext.asyncio import AsyncSession
from .models import Person
from app.models import PersonForm


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
