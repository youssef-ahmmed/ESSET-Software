from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ChannelPins(Base):

    __tablename__ = 'channel_pins'

    id = Column('id', Integer, primary_key=True)
    channel_name = Column('channel_name', String(50), nullable=False)
    direction = Column('direction', String(10), nullable=False)
    hardware_pin = Column('hardware_pin', String(20), nullable=False)
