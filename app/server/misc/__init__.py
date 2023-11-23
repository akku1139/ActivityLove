from . import hostmeta, nodeinfo, webfinger

routes = hostmeta.routes + nodeinfo.routes + webfinger.routes
