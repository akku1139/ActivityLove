# https://yamaimo.hatenablog.jp/entry/2023/09/01/220000
import kumade as ku  # ライブラリのインポート

@ku.task("create_db")
def create_db():
  from db.setting import engine, Base
  Base.metadata.create_all(bind=engine)
