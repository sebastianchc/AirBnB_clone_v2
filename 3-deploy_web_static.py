#!/usr/bin/python3
from fabric.api import local, put, env, run
from datetime import datetime
from os import path


env.hosts = ["35.237.254.152", "35.196.237.181"]
env.user = "ubuntu"


def deploy():
    try:
        archive_path = do_pack()
    except:
        return False
    return do_deploy(archive_path)


def do_pack():
    try:
        local("mkdir -p versions")
        date = datetime.now()
        path = date.strftime("%Y%m%d%H%M%S")
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(path))
        return "web_static_{}".format(path)
    except:
        return None


def do_deploy(archive_path):
    if not path.isfile(archive_path):
        return False
    compress_f = archive_path.split("/")
    compress_f = compress_f[-1]
    compress_f = path.splitext(compress_f)
    file_name = compress_f[0]
    extension = compress_f[1]
    path_file = "{}{}".format(file_name, extension)
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(file_name))
        uncompress = "tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
        run(uncompress.format(path_file, file_name))
        run("rm /tmp/{}".format(path_file))
        move1 = "mv /data/web_static/releases/{}/web_static/*"
        move2 = "/data/web_static/releases/{}/"
        move = "{} {}".format(move1, move2)
        run(move.format(file_name, file_name))
        run("rm -fr /data/web_static/current")
        s_link = "ln -s /data/web_static/releases/{} /data/web_static/current"
        run(s_link.format(file_name))
        return True
    except Exception as error:
        print(error)
        return False
