from db.setting import Base
from sqlalchemy import Column, String, DateTime

class Account(Base):
  __tablename__ == "account"

  id = Column("id", String, primary_key=True)

class Profile(Base):
  __tablename__:str = "user"

  id = Column("id", String, primary_key=True)

  name = Column("name", String)
  profile = Column("profile", String)

  created_at = Column("created_at", DateTime)
  private_key = Column("private_key", String)
  public_key = Column("publoc_key", String)
