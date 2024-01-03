from db.setting import Base
from sqlalchemy import Column, String, DateTime

class Password(Base):
  __tablename__:str = "auth_password"

  user = Column("user", String)

  created_at = Column("created_at", DateTime)
