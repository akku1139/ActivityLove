from db.setting import get_session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.model.user import User

async def find_user(db:AsyncSession, id:str) -> bool:
  if (await (db.excute(select(User).filter(User.id == id)))) is None:
    return False
  else:
    return True
