from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import (
    String,
    # Integer,
    DateTime,
    func
)


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(primary_key=True)
    # tg_user_id: Mapped[int] = mapped_column(Integer, index=True)

    name: Mapped[str] = mapped_column(String(100))
    city: Mapped[str] = mapped_column(String(100))

    created_at: Mapped[str] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
