from sqlalchemy import Column, Integer, String, DateTime, CheckConstraint

from models.entities import Base


class SniffedData(Base):

    __tablename__ = 'sniffed_data'

    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=False)
    time_taken = Column(Integer, nullable=False)
    connection_way = Column(String(10), nullable=False)
    communication_protocol_name = Column(String(10))

    __table_args__ = (
        CheckConstraint("connection_way LIKE '_Bit'"),
        CheckConstraint("communication_protocol_name IN ('uart', 'spi', 'i2c')")
    )
