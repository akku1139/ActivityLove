from db.setting import get_session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.model.user import User

async def find_user(db:AsyncSession, id:str) -> bool:
  if (await (db.execute(select(User).filter(User.id == id)))).first() is None:
    return False
  else:
    return True
