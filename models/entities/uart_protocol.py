from sqlalchemy import Column, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UartProtocol(Base):

    __tablename__ = 'uart_protocols'

    id = Column('id', Integer, primary_key=True)
    input_channel_number = Column('input_channel_number', Integer, nullable=False)
    output_channel_number = Column('output_channel_number', Integer, nullable=False)
    clocks_per_bit = Column('clocks_per_bit', Integer, default=217)
    baud_rate = Column('baud_rate', Integer, default=115200)
    data_size = Column('data_size', Integer, default=8)
    stop_bit = Column('stop_bit', Integer, default=1)
    parity_bit = Column('parity_bit', CHAR, default='N')
