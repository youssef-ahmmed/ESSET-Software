from sqlalchemy import Column, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class OneBitSniffing(Base):

    __tablename__ = 'one_bit_sniffing'

    id = Column('id', Integer, primary_key=True)
    output_channel_number = Column('output_channel_number', Integer, nullable=False)
