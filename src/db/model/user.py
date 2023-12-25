from db.setting import Base
from sqlalchemy import Column, Integer, String, DateTime

class User(Base):
  __tablename__:str = "user"

  id = Column("id", String)
  private_key = Column("private_key", String)
  public_key = Column("publoc_key", String)
