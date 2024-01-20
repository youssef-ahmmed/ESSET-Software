from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}]"
