from sqlalchemy import Column, Integer
from base_table import Base


class NBitSniffing(Base):

    __tablename__ = 'n_bits_sniffing'

    id = Column('id', Integer, primary_key=True)
    channel_numbers = Column('channel_numbers', Integer, nullable=False)
