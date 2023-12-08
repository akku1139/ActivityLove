from info.config import conf

match conf["db"]["type"]:
  case "postgres":
    pass
  
  case "sqlite":
    pass
  
  case "mysql":
    pass
  
  case "json":
    import wrapper.json
    db = wrapper.json.JSONDB