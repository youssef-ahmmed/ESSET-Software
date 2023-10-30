from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.entities import Base


class OneBit(Base):
    __tablename__ = 'one_bit'

    id = Column('Id', Integer, primary_key=True)
    sniffed_data_id = Column('sniffedDataId', Integer, ForeignKey('sniffed_data.id'))
    output_channel_number = Column('outputChannelNumber', Integer, nullable=False, default=8)
    sniffed_data = relationship('SniffedData', backref='one_bit', cascade='all, delete')
