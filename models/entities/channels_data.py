from sqlalchemy import Column, Integer, ForeignKey, BLOB
from sqlalchemy.orm import relationship

from models.entities.base_model import Base, BaseModel


class ChannelsData(BaseModel, Base):
    __tablename__ = 'channels_data'

    id = Column(Integer, primary_key=True)
    sniffed_data_id = Column(Integer, ForeignKey('sniffed_data.id'))
    channel_number = Column(Integer, nullable=False)
    channel_data = Column(BLOB)

    sniffed_data = relationship('SniffedData', backref='channels_data', cascade='all, delete')
