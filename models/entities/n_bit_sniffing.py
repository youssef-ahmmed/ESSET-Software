from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.entities.base_model import Base, BaseModel


class NBit(BaseModel, Base):
    __tablename__ = 'n_bit'

    id = Column(Integer, primary_key=True)
    sniffed_data_id = Column(Integer, ForeignKey('sniffed_data.id'))
    channel_number = Column(Integer, nullable=False)
    clock_rate = Column(Integer, nullable=False)

    sniffed_data = relationship('SniffedData', backref='n_bit', cascade='all, delete')
