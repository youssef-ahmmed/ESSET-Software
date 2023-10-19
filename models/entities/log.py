from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Log(Base):

    __tablename__ = 'logs'

    id = Column('id', Integer, primary_key=True)
    created_at = Column('created_at', DateTime, nullable=False, default=datetime.utcnow())
    description = Column('description', String(1024), nullable=False)
