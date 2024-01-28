from sqlalchemy import Column, Integer, String, DateTime, CheckConstraint

from models.entities.base_model import Base, BaseModel


class SniffedData(BaseModel, Base):
    __tablename__ = 'sniffed_data'

    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=False)
    time_taken = Column(Integer, nullable=False)
    connection_way = Column(String(10))
    communication_protocol_name = Column(String(10))

    __table_args__ = (
        CheckConstraint("connection_way IN ('1Bit', 'NBits')"),
        CheckConstraint("communication_protocol_name IN ('UART', 'SPI', 'I2C')")
    )
