from . import hostmeta, manifest, nodeinfo, webfinger

routes = hostmeta.routes + manifest.routes + nodeinfo.routes + webfinger.routes
