import os
import importlib
import asyncio

files = sorted(os.listdir("."))

for file in files:
  if (file != "main.py") and (file != "__pycache__") :
    m = importlib.import_module(file.removesuffix(".py"))
    asyncio.run(m.run())
