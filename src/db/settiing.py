from info.config import conf

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 接続先DBの設定
# https://docs.sqlalchemy.org/en/20/core/engines.html
if conf["db"]["dialect"] == "sqlite":
  DATABASE = "sqlite:///../../"+conf["db"]["database"]
else:
  if conf["db"]["driver"] != "":
    drivername = f'{conf["db"]["dialect"]}+{conf["db"]["driver"]}'
  else:
    drivername = conf["db"]["dialect"]

  from sqlalchemy import URL
  DATABASE = URL.create(
    drivername,
    username = conf["db"]["user"],
    password = conf["db"]["pass"],
    host = conf["db"]["host"],
    port = conf["db"]["port"],
    database = conf["db"]["detabase"]
  )


engine = create_async_engine(
  DATABASE,
  encoding="utf-8",
  echo=False
)

async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass


async def get_session():
    async with async_session() as session:
        yield session
