#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    try:
        local("mkdir -p versions")
        date = datetime.now()
        path = date.strftime("%Y%m%d%H%M%S")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(path))
        return "web_static_{}".format(path)
    except:
        return None
