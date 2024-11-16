from sqlalchemy.orm import Mapped, mapped_column
from config import Base

class User(Base):
    __tablename__ = 'users'