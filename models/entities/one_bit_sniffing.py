from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.entities import Base


class OneBit(Base):
    __tablename__ = 'one_bit'

    id = Column('id', Integer, primary_key=True)
    sniffed_data_id = Column('sniffed_data_id', Integer, ForeignKey('sniffed_data.id'))
    output_channel_number = Column('output_channel_number', Integer, nullable=False, default=8)
    sniffed_data = relationship('SniffedData', backref='one_bit', cascade='all, delete')
