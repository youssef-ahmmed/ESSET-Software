from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.entities import Base


class ChannelPins(Base):

    __tablename__ = 'channel_pins'

    id = Column(Integer, primary_key=True)
    sniffed_data_id = Column(Integer, ForeignKey('sniffed_data.id'))
    channel_name = Column(String(50), nullable=False)
    direction = Column(String(10), nullable=False)
    hardware_pin = Column(String(20), nullable=False)

    sniffed_data = relationship('SniffedData', backref='channel_pins', cascade='all, delete')
