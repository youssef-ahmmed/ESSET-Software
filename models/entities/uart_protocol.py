from sqlalchemy import Column, Integer, CHAR, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship

from models.entities import Base


class Uart(Base):
    __tablename__ = 'uart'

    id = Column('id', Integer, primary_key=True)
    sniffed_data_id = Column(Integer, ForeignKey('sniffed_data.id'))
    clk_per_bit = Column(Integer, nullable=False, default=217)
    baud_rate = Column(Integer, nullable=False, default=115200)
    data_size = Column(Integer, nullable=False, default=8)
    stop_bit = Column(Integer, default=1)
    parity_bit = Column(CHAR(1), default='N')
    sniffed_data = relationship('SniffedData', backref='uart', cascade='all, delete')

    __table_args__ = (
        CheckConstraint("parity_bit IN ('N', 'E', 'O')"),
    )
