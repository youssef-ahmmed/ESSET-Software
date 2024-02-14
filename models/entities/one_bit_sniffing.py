from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.entities.base_model import Base, BaseModel


class OneBit(BaseModel, Base):
    __tablename__ = 'one_bit'

    id = Column(Integer, primary_key=True)
    sniffed_data_id = Column(Integer, ForeignKey('sniffed_data.id'))
    output_channel_number = Column(Integer, nullable=False, default=8)
    clock_rate = Column(Integer, nullable=False)

    sniffed_data = relationship('SniffedData', backref='one_bit', cascade='all, delete')
