from db.setting import engine, Base
from db.model.user import User

async def run():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
