from sqlalchemy import Column, Integer, CHAR
from base_table import Base


class OneBitSniffing(Base):

    __tablename__ = 'one_bit_sniffing'

    id = Column('id', Integer, primary_key=True)
    output_channel_number = Column('output_channel_number', Integer, nullable=False)
