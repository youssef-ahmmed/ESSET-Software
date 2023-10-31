from sqlalchemy import Column, Integer, CHAR, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship

from models.entities import Base


class Spi(Base):
    __tablename__ = 'spi'

    id = Column('id', Integer, primary_key=True)
    sniffed_data_id = Column('sniffed_data_id', Integer, ForeignKey('sniffed_data.id'))
    significant_bit = Column('significant_bit', CHAR(1), nullable=False, default='M')
    clk_state = Column('clk_state', Integer, nullable=False, default=0)
    clk_phase = Column('clk_phase', Integer, nullable=False, default=0)
    data_size = Column('data_size', Integer, nullable=False, default=8)
    sniffed_data = relationship('SniffedData', backref='spi', cascade='all, delete')

    __table_args__ = (
        CheckConstraint("significant_bit IN ('M', 'L')"),
    )
