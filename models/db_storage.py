from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from entities.base_table import Base


class DBStorage:
    __url_db = "mysql+mysqldb://{}:{}@{}/{}".format(
        getenv('MYSQL_USER'),
        getenv('MYSQL_PWD'),
        getenv('MYSQL_HOST'),
        getenv('MYSQL_DB')
    )
    __session = None

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
