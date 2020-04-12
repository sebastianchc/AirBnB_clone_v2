#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    try:
        local("mkdir -p versions")
        date = datetime.now()
        date = date.strftime("%Y%m%d%H%M%S")
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
        return "web_static_{}".format(date)
    except:
        return None
