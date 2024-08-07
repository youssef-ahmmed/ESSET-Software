from sqlalchemy import Column, Integer, CHAR, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship
from models.entities.base_model import Base, BaseModel


class Spi(BaseModel, Base):
    __tablename__ = 'spi'

    id = Column(Integer, primary_key=True)
    sniffed_data_id = Column(Integer, ForeignKey('sniffed_data.id'))
    clock_rate = Column(Integer, nullable=False)
    significant_bit = Column(CHAR(1), nullable=False, default='M')
    clk_state = Column(Integer, nullable=False, default=0)
    clk_phase = Column(Integer, nullable=False, default=0)
    data_size = Column(Integer, nullable=False, default=8)

    sniffed_data = relationship('SniffedData', backref='spi', cascade='all, delete')

    __table_args__ = (
        CheckConstraint("significant_bit IN ('M', 'L')"),
    )
