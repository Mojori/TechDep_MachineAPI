from sqlalchemy import ForeignKey, insert, delete, update
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session
from sqlalchemy import select


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


from sqlalchemy import create_engine

engine = create_engine("sqlite:///dbtest.db", echo=False)

Base.metadata.create_all(engine)


def create_user(user_name):
    with Session(engine) as session:
        stmt = insert(User).values(
            name=user_name,
        )
        session.execute(stmt)
        session.commit()


def create_car(car_name):
    with Session(engine) as session:
        stmt = insert(Car).values(
            name=car_name,
        )
        session.execute(stmt)
        session.commit()


def create_order(user_id: int, car_id: int):
    with Session(engine) as session:
        stmt = insert(Order).values(
            user_id=user_id,
            car_id=car_id
        )
        session.execute(stmt)
        session.commit()


def get_all_orders():
    all_res = {}
    with Session(engine) as session:
        stmt = (
            select(Order)
            .join(Order.user)
            .join(Order.car)
        )
        for order_info in session.scalars(stmt):
            res = {
                "id": order_info.id,

                "user":
                    {
                        "user id": order_info.user.id,
                        "user name": order_info.user.name
                    },

                "car":
                    {
                        "car id": order_info.car.id,
                        "car name": order_info.car.name
                    }

            }
            all_res[order_info.id] = res
    print(all_res)
    return all_res


def get_all_cars():
    all_res = {}
    with Session(engine) as session:
        stmt = (
            select(Car)
        )
        for car_info in session.scalars(stmt):
            res = {
                "id": car_info.id,
                "name": car_info.name
            }
            all_res[car_info.id] = res
    print(all_res)
    return all_res


def get_all_users():
    all_res = {}
    with Session(engine) as session:
        stmt = (
            select(User)
        )
        for user_info in session.scalars(stmt):
            res = {
                "id": user_info.id,
                "name": user_info.name
            }
            all_res[user_info.id] = res
    print(all_res)
    return all_res


def delete_user(user_id):
    with Session(engine) as session:
        stmt = (
            delete(User)
            .where(User.id == user_id)
        )
        session.execute(stmt)
        session.commit()


def delete_car(car_id):
    with Session(engine) as session:
        stmt = (
            delete(Car)
            .where(Car.id == car_id)
        )
        session.execute(stmt)
        session.commit()


def delete_order(order_id):
    with Session(engine) as session:
        stmt = (
            delete(Order)
            .where(Order.id == order_id)
        )
        session.execute(stmt)
        session.commit()


def update_user(user_id, name):
    with Session(engine) as session:
        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(
                {
                    User.name: name
                }
            )
        )
        session.execute(stmt)
        session.commit()


def update_car(car_id, name):
    with Session(engine) as session:
        stmt = (
            update(Car)
            .where(Car.id == car_id)
            .values(
                {
                    Car.name: name
                }
            )
        )
        session.execute(stmt)
        session.commit()


def update_order(order_id, user_id, car_id):
    with Session(engine) as session:
        stmt = (
            update(Order)
            .where(Order.id == order_id)
            .values(
                {
                    Order.user_id: user_id,
                    Order.car_id: car_id

                }
            )
        )
        session.execute(stmt)
        session.commit()



"""tests"""
def create_table():
    create_user("us_test1")
    create_car("car_test1")
    create_user("us_test2")
    create_car("car_test2")
    create_order(1, 1)
    create_order(2, 2)