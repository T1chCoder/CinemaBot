from sqlalchemy.orm import Mapped, mapped_column
import config

class User(config.Base):
    __tablename__ = 'users'