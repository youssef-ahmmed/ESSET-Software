from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.entities.base_model import Base, BaseModel


class ChannelPins(BaseModel, Base):
    __tablename__ = 'channel_pins'

    id = Column(Integer, primary_key=True)
    sniffed_data_id = Column(Integer, ForeignKey('sniffed_data.id'))
    channel_name = Column(String(50), nullable=False)
    hardware_pin = Column(String(20), nullable=False)

    sniffed_data = relationship('SniffedData', backref='channel_pins', cascade='all, delete')
