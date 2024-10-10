from sqlalchemy import insert
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from models import Base, User, Car, Order

engine = create_engine("sqlite:///dbtest.db", echo=False)

Base.metadata.create_all(engine)

"""----------TEST----------"""


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


def create_table():
    create_user("us_test1")
    create_car("car_test1")
    create_user("us_test2")
    create_car("car_test2")
    create_order(1, 1)
    create_order(2, 2)

# create_table()
