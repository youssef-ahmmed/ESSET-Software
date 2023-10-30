from sqlalchemy import Column, Integer, CHAR, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship

from models.entities import Base


class Spi(Base):
    __tablename__ = 'spi'

    id = Column('Id', Integer, primary_key=True)
    sniffed_data_id = Column('SniffedDataId', Integer, ForeignKey('sniffed_data.id'))
    significant_bit = Column('Significant Bit', CHAR(1), nullable=False, default='M')
    clk_state = Column('Clk State', Integer, nullable=False, default=0)
    clk_phase = Column('Clk Phase', Integer, nullable=False, default=0)
    data_size = Column('Data Size', Integer, nullable=False, default=8)
    sniffed_data = relationship('SniffedData', backref='spi', cascade='all, delete')

    __table_args__ = (
        CheckConstraint("significant_bit IN ('M', 'L')"),
    )
