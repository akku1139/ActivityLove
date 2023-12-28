from info.config import conf
import info.software as soft
import info.statistics as stat

# だいたい同じなので同じものを返す。
# 1系を使っているサーバーは知らないので問題なし。

# https://github.com/jhass/nodeinfo/blob/main/schemas/2.0/schema.json
# https://github.com/jhass/nodeinfo/blob/main/schemas/2.1/schema.json

nodeinfo2: dict = {
  "version": "2.1",
  "software": {
    "name": soft.name,
    "version": soft.version,
    "repository": soft.repository,
    "homepage": soft.homepage
  },
  "protocols": [
    "activitypub"
  ],
  "services": {
    # TODO RSSとかAtomとか対応したいね。
    "inbound": [],
    "outbound": []
  },
  "openRegistrations": conf["open_registrations"],
  "usage": {
    "users": {
      "total": stat.users,
      "activeHalfyear": None,
      "activeMonth": None
    },
    "localPosts": stat.posts,
    "localComments": 0
  },
  "metadata": {
    "nodeName": conf["name"],
    "nodeDescription": conf["description"],
    "maxNoteTextLength": conf["max_note_text_length"],
    "proxyAccountName": conf["proxy_account_name"],
    "themeColor": conf["theme_color"],
    "maintainer": {
      "name": conf["maintainer_name"],
      "email": conf["maintainer_email"]
    }
  },
}
