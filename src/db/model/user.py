from db.setting import Base
from sqlalchemy import Column, String, DateTime

class User(Base):
  __tablename__:str = "user"

  id = Column("id", String)

  name = Column("name", String)
  profile = Column("profile", String)

  created_at = Column("created_at", DateTime)
  private_key = Column("private_key", String)
  public_key = Column("publoc_key", String)
