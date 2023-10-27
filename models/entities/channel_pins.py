from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.entities import Base


class ChannelPins(Base):

    __tablename__ = 'channel_pins'

    id = Column('id', Integer, primary_key=True)
    channel_name = Column('channel_name', String(50), nullable=False)
    direction = Column('direction', String(10), nullable=False)
    hardware_pin = Column('hardware_pin', String(20), nullable=False)
    sniffed_data = relationship('SniffedData', backref='channel_pins', cascade='all, delete')
