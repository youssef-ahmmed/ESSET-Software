from os import getenv

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, scoped_session, aliased
import sqlite3

from models.entities.base_model import Base
from models.entities.sniffed_data import SniffedData
from models.entities.channel_pins import ChannelPins
from models.entities.n_bit_sniffing import NBit
from models.entities.one_bit_sniffing import OneBit
from models.entities.spi_protocol import Spi
from models.entities.uart_protocol import Uart
from models.entities.channels_data import ChannelsData


class DBStorage:
    __url_mysqldb = "mysql+mysqldb://esset_dev:esset_dev_pwd@localhost/esset_dev_db"
    __url_sqlitedb = "sqlite:///esset.db"
    __session = None
    __engine = None

    def __init__(self):
        self.__engine = create_engine(self.__url_sqlitedb, pool_pre_ping=True)

    def save(self):
        self.__session.commit()

    def insert(self, obj):
        self.__session.add(obj)

    def get_by_id(self, cls, id):
        return self.__session.query(cls).get(id)

    def get_last_id(self, cls):
        max_id = self.__session.query(func.max(cls.id)).scalar()
        return max_id

    def get_data_by_start_time(self, start_time):
        cd = aliased(ChannelsData)
        sd = aliased(SniffedData)

        return self.__session.query(cd.channel_data).join(sd, cd.sniffed_data_id == sd.id).filter(sd.start_time == start_time).all()

    def list_all(self, cls):
        return self.__session.query(cls).all()

    def delete(self, obj):
        self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
