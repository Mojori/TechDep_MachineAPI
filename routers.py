from fastapi import APIRouter
from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import Session
from database import engine
from models import User, Car, Order

from schema import UserSchema, GetId, CarSchema, OrderSchema

api_router = APIRouter()

"""
ORDER
"""


@api_router.post("/api/order", tags=["Orders"], response_model=UserSchema)
def create_order(input_data: OrderSchema):
    user_id = input_data.user_id
    car_id = input_data.car_id
    with Session(engine) as session:
        stmt = insert(Order).values(
            user_id=user_id,
            car_id=car_id
        )
        session.execute(stmt)
        session.commit()

    return {
        "user_id": user_id,
        "car_id": car_id
    }


@api_router.get("/api/order/get-all", tags=["Orders"])
def get_all_orders():
    all_res = []
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
            all_res.append(res)
    return all_res


@api_router.post("/api/order/{orderID}", tags=["Orders"])
def get_order_by_id(input_data: GetId):
    order_id = input_data.id
    with Session(engine) as session:
        stmt = (
            select(Order)
            .where(Order.id == order_id)
        )
        order_info = session.scalar(stmt)

    return {
        "id": order_info.id,
        "name_id": order_info.user_id,
        "car_id": order_info.car_id
    }


@api_router.delete("/api/order/{orderID}", tags=["Orders"])
def delete_orders_by_id(input_data: GetId):
    order_id = input_data.id
    with Session(engine) as session:
        stmt = (
            delete(Order)
            .where(Order.id == order_id)
        )
        session.execute(stmt)
        session.commit()

    return True


@api_router.patch("/api/order/{orderID}", tags=["Orders"])
def update_order_by_id(input_data: OrderSchema):
    order_id = input_data.id
    order_user_id = input_data.user_id
    order_car_id = input_data.car_id

    with Session(engine) as session:
        stmt = (
            update(Order)
            .where(Order.id == order_id)
            .values(
                {
                    Order.user_id: order_user_id,
                    Order.car_id: order_car_id
                }
            )
        )
        session.execute(stmt)
        session.commit()
    return True


"""
CAR
"""


@api_router.post("/api/car", tags=["Cars"])
def create_car(input_data: CarSchema):
    car_name = input_data.name
    with Session(engine) as session:
        stmt = insert(Car).values(
            name=car_name,
        )
        session.execute(stmt)
        session.commit()

    return {
        "name": car_name
    }


@api_router.get("/api/car/get-all", tags=["Cars"])
def get_all_cars():
    all_res = []
    with Session(engine) as session:
        stmt = (
            select(Car)
        )
        for car_info in session.scalars(stmt):
            res = {
                "id": car_info.id,
                "name": car_info.name
            }
            all_res.append(res)
    return all_res


@api_router.post("/api/car/{carID}", tags=["Cars"], response_model=CarSchema)
def get_car_by_id(input_data: GetId):
    car_id = input_data.id
    with Session(engine) as session:
        stmt = (
            select(Car)
            .where(Car.id == car_id)
        )
        car_info = session.scalar(stmt)

    return {
        "id": car_info.id,
        "name": car_info.name
    }


@api_router.delete("/api/car/{carID}", tags=["Cars"])
def delete_cars_by_id(input_data: GetId):
    car_id = input_data.id
    with Session(engine) as session:
        stmt = (
            delete(Car)
            .where(Car.id == car_id)
        )
        session.execute(stmt)
        session.commit()

    return True


@api_router.patch("/api/car/{carID}", tags=["Cars"])
def update_car_by_id(input_data: CarSchema):
    car_id = input_data.id
    car_name = input_data.name
    with Session(engine) as session:
        stmt = (
            update(Car)
            .where(Car.id == car_id)
            .values(
                {
                    Car.name: car_name
                }
            )
        )
        session.execute(stmt)
        session.commit()
    return True


"""
USER
"""


@api_router.post("/api/user", tags=["Users"])
def create_user(input_data: UserSchema):
    user_name = input_data.name
    with Session(engine) as session:
        stmt = insert(User).values(
            name=user_name,
        )
        session.execute(stmt)
        session.commit()

    return {
        "name": user_name
    }


@api_router.get("/api/user/get-all", tags=["Users"])
def get_all_users():
    all_res = []
    with Session(engine) as session:
        stmt = (
            select(User)
        )
        for user_info in session.scalars(stmt):
            res = {
                "id": user_info.id,
                "name": user_info.name
            }
            all_res.append(res)
    return all_res


@api_router.post("/api/user/{userID}", tags=["Users"], response_model=UserSchema)
def get_user_by_id(input_data: GetId):
    user_id = input_data.id
    with Session(engine) as session:
        stmt = (
            select(User)
            .where(User.id == user_id)
        )
        user_info = session.scalar(stmt)

    return {
        "id": user_info.id,
        "name": user_info.name
    }


@api_router.delete("/api/user/{userID}", tags=["Users"])
def delete_users_by_id(input_data: GetId):
    user_id = input_data.id
    with Session(engine) as session:
        stmt = (
            delete(User)
            .where(User.id == user_id)
        )
        session.execute(stmt)
        session.commit()

    return True


@api_router.patch("/api/user/{userID}", tags=["Users"])
def update_user_by_id(input_data: UserSchema):
    user_id = input_data.id
    user_name = input_data.name
    with Session(engine) as session:
        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(
                {
                    User.name: user_name
                }
            )
        )
        session.execute(stmt)
        session.commit()
    return True
