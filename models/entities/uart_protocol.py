from sqlalchemy import Column, Integer, CHAR, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship

from models.entities import Base


class Uart(Base):
    __tablename__ = 'uart'

    id = Column('id', Integer, primary_key=True)
    sniffed_data_id = Column('SniffedDataId', Integer, ForeignKey('sniffed_data.id'))
    clk_per_bit = Column('Clk Per Bit', Integer, nullable=False, default=217)
    baud_rate = Column('Baud Rate', Integer, nullable=False, default=115200)
    data_size = Column('Data Size', Integer, nullable=False, default=8)
    stop_bit = Column('Stop Bit', Integer, default=1)
    parity_bit = Column('Parity Bit', CHAR(1), default='N')
    sniffed_data = relationship('SniffedData', backref='uart', cascade='all, delete')

    __table_args__ = (
        CheckConstraint("parity_bit IN ('N', 'E', 'O')"),
    )
