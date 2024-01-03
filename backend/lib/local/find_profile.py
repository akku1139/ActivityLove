from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.model.user import Profile

async def find_user(db:AsyncSession, id:str) -> bool:
  if (await (db.execute(select(Profile).filter(Profile.id == id)))).first() is None:
    return False
  else:
    return True
