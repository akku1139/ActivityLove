from db.setting import engine, Base
import glob
import importlib

p:str
for p in glob.glob("**/*.py", root_dir="../src/db/model/", recursive=True):
  importlib.import_module("db.model."+(p.removesuffix(".py").replace("/", ".")))

async def run():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
