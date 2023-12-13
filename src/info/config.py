from pathlib import Path
import tomllib
path: Path = Path(__file__).parent.parent.parent/"config"/"default.toml"

with open(path, 'rb') as fp:
  conf: dict = tomllib.load(fp)
