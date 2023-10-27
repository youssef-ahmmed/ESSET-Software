from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import sqlite3

from models.entities import Base
from models.entities.sniffed_data import SniffedData
from models.entities.channel_pins import ChannelPins
from models.entities.log import Log
from models.entities.n_bit_sniffing import NBit
from models.entities.one_bit_sniffing import OneBit
from models.entities.spi_protocol import Spi
from models.entities.uart_protocol import Uart


class DBStorage:
    # __url_db = "mysql+mysqldb://esset_dev:esset_dev_pwd@localhost/esset_dev_db"
    __url_db = "sqlite:///site.db"
    __session = None
    __engine = None

    def __init__(self):
        self.__engine = create_engine(self.__url_db, pool_pre_ping=True)

    def save(self):
        self.__session.commit()

    def reload(self):
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
