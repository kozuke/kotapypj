from sqlalchemy import Column, Integer, DATETIME, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AccessLog(Base):
    __tablename__ = 'access_log'
    id = Column('id', Integer, primary_key=True)
    access_time = Column('access_time', DATETIME, nullable=False, server_default=text('NOW()'))
    access_count = Column('access_count', Integer, nullable=False, server_default='0')
