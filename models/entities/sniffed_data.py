from sqlalchemy import Column, Integer, String, DateTime, BLOB, CheckConstraint

from models.entities import Base


class SniffedData(Base):
    __tablename__ = 'sniffed_data'

    id = Column('id', Integer, primary_key=True)
    start_time = Column('start_time', DateTime, nullable=False)
    time_taken = Column('time_taken', Integer, nullable=False)
    data = Column('data', BLOB)
    connection_way = Column('connection_way', String(10), nullable=False)
    communication_protocol_name = Column('communication_protocol_name', String(10))

    __table_args__ = (
        CheckConstraint("connection_way LIKE '_Bit'"),
        CheckConstraint("communication_protocol_name IN ('uart', 'spi', 'i2c')")
    )
