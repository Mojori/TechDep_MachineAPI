from typing import Optional, Literal, List
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session


class Base(DeclarativeBase):
    pass


Status = Literal["pending", "received", "completed"]


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str]

    orders: Mapped[List["Order"]] = relationship(back_populates="user")


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)

    # UID: Mapped[str] = mapped_column(unique=True)
    # status: Mapped[Status]

    date: Mapped[str]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="orders")

    car_id: Mapped[List[int]]


class Car(Base):
    __tablename__ = "cars"
    id: Mapped[int] = mapped_column(primary_key=True)

    car_name: Mapped[str]

    brand: Mapped[str]
    price: Mapped[float]
    data: Mapped[str]
    used: Mapped[bool]
    number: Mapped[Optional[str]]
    color: Mapped[str]

from sqlalchemy import create_engine

engine = create_engine("sqlite:///dbtest.db", echo=True)

Base.metadata.create_all(engine)

with Session(engine) as session:

    test = User(name="test", password="test")
    session.add_all([test,])
    session.commit()
