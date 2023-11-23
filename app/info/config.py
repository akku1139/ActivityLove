import tomllib
from pathlib import Path
from lib.dict2 import dict2

path = Path(__file__).parent.parent.parent/"config"/"default.toml"

with open(path, 'rb') as fin:
  conf = dict2(tomllib.load(fin))
