from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, BLOB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SniffedData(Base):

    __tablename__ = 'sniffed_data'

    id = Column('id', Integer, primary_key=True)
    start_at = Column('start_at', DateTime, nullable=False, default=datetime.utcnow())
    timer = Column('timer', Integer, nullable=False)
    binary_data = Column('binary_data', BLOB)
    text_data = Column('text_data', String(1024))
