import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def default_engine():
    user_name = os.environ['MYSQL_USER_NAME']
    password = os.environ['MYSQL_PASSWORD']
    db_driver_name = f'mysql://{user_name}:{password}@localhost/kotapypj'
    return create_engine(db_driver_name)


class DB:

    def __init__(self, engine):
        self.engine = engine

    def insert(self, model):
        session = sessionmaker(bind=self.engine)()
        session.add(model)
        session.commit()
