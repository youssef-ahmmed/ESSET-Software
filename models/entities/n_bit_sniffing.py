from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NBitSniffing(Base):

    __tablename__ = 'n_bits_sniffing'

    id = Column('id', Integer, primary_key=True)
    channel_numbers = Column('channel_numbers', Integer, nullable=False)
