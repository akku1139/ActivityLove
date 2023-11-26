import tomllib
from pathlib import Path

path: Path = Path(__file__).parent.parent.parent/"config"/"default.toml"

with open(path, 'rb') as fin:
  conf: dict = tomllib.load(fin)
