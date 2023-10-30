from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.entities import Base


class NBit(Base):
    __tablename__ = 'n_bit'

    id = Column('Id', Integer, primary_key=True)
    sniffed_data_id = Column('SniffedDataId', Integer, ForeignKey('sniffed_data.id'))
    channel_number = Column('ChannelNumber', Integer, nullable=False)
    sniffed_data = relationship('SniffedData', backref='n_bit', cascade='all, delete')
