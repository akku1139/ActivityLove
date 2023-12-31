from info.config import conf

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs

import os

# 接続先DBの設定
# https://docs.sqlalchemy.org/en/20/core/engines.html
if conf["db"]["dialect"] == "sqlite":
  # pysqliteはaioじゃなくて使えないので必ず他ドライバーを使うこと。
  DATABASE = f'sqlite+{conf["db"]["driver"]}:///{os.path.dirname(__file__)}/../../{conf["db"]["database"]}'
else:
  if conf["db"]["driver"] != "":
    drivername = f'{conf["db"]["dialect"]}+{conf["db"]["driver"]}'
  else:
    # 多分ここに流れてくることはない。
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
  # DBごとに変えないといけない可能性ある
  # https://github.com/search?q=repo%3Asqlalchemy%2Fsqlalchemy%20encoding&type=code
  # encoding="utf-8",
  echo=False
)

async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
  pass
