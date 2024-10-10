from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(30), unique=True)
    orders: Mapped["Order"] = relationship(back_populates="user")


class Car(Base):
    __tablename__ = "cars"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]
    orders: Mapped["Order"] = relationship(back_populates="car")


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("cars.id"))
    user: Mapped["User"] = relationship(back_populates="orders")
    car: Mapped["Car"] = relationship(back_populates="orders")
