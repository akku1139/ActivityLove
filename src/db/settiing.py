from info.config import conf

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
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
    dialect,
    username = conf["db"]["user"],
    password = conf["db"]["pass"],
    host = conf["db"]["host"],
    port = conf["db"]["port"],
    database = conf["db"]["detabase"]
  )


# Engine の作成
Engine = create_engine(
  DATABASE,
  encoding="utf-8",
  echo=False
)
Base = declarative_base()

# Sessionの作成
session = Session(
  autocommit = False,
  autoflush = True,
  bind = Engine
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()
