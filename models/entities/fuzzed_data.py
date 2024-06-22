from sqlalchemy import Column, Integer, String, Float

from models.entities.base_model import Base, BaseModel


class FuzzedData(BaseModel, Base):
    __tablename__ = 'fuzzed_data'

    id = Column(Integer, primary_key=True)
    message = Column(String, nullable=False)
    message_length = Column(Integer, nullable=False)
    message_entropy = Column(Float, nullable=False)
    response = Column(String, nullable=True)
    response_length = Column(String, nullable=True)
    response_entropy = Column(Float, nullable=True)
