# 抽象クラス
from abc import ABC, abstractmethod

# asyncするか迷うところ。
class DB(ABC):
  @abstractmethod
  def __init__(self, table: str):
    pass
  
  # キーから取得する
  @abstractmethod
  def get(self, key: str):
    pass
  
  # キーに対して設置する
  @abstractmethod
  def put(self, key: str, obj):
    pass