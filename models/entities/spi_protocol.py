from sqlalchemy import Column, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SpiProtocol(Base):

    __tablename__ = 'spi_protocols'

    id = Column('id', Integer, primary_key=True)
    input_channel_number = Column('input_channel_number', Integer, nullable=False)
    output_channel_number = Column('output_channel_number', Integer, nullable=False)
    significant_bit = Column('significant_bit', CHAR, default='M')
    data_size = Column('data_size', Integer, default=8)
    clock_state = Column('clock_state', Integer, default=0)
    clock_phase = Column('clock_phase', Integer, default=0)
