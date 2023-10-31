from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.entities import Base


class NBit(Base):
    __tablename__ = 'n_bit'

    id = Column('id', Integer, primary_key=True)
    sniffed_data_id = Column('sniffed_data_id', Integer, ForeignKey('sniffed_data.id'))
    channel_number = Column('channel_number', Integer, nullable=False)
    sniffed_data = relationship('sniffed_data', backref='n_bit', cascade='all, delete')
