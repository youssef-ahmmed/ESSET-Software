from sqlalchemy import Column, Integer, String, DateTime, BLOB, CheckConstraint

from models.entities import Base


class SniffedData(Base):
    __tablename__ = 'sniffed_data'

    id = Column('Id', Integer, primary_key=True)
    start_time = Column('Start Time', DateTime, nullable=False)
    time_taken = Column('Time Taken', Integer, nullable=False)
    data = Column('Data', BLOB)
    connection_way = Column('Connection Way', String(10), nullable=False)
    communication_protocol_name = Column('Communication Protocol Name', String(10))

    __table_args__ = (
        CheckConstraint("connection_way LIKE '_Bit'"),
        CheckConstraint("communication_protocol_name IN ('uart', 'spi', 'i2c')")
    )
