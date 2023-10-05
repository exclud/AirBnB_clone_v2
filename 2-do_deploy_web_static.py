#!/usr/bin/python3
"""Distributes an archive to web servers."""
from fabric.api import run, put, env, local
import os


env.hosts = ['54.157.176.235', '54.144.223.110']
# Optional: Define these if not using default SSH keys and usernames.
# env.user = "shammah"
# env.key_filename = "/ssh/id_rsa/"


def do_deploy(archive_path):
    """Distributes an archive to web servers."""

    if not os.path.exists(archive_path):
        return False

    # Extracting the filename without the full path
    file_name = os.path.basename(archive_path)
    name_without_ext = file_name.split('.')[0]

    remote_path = "/tmp/{}".format(file_name)
    data_path = "/data/web_static/releases/{}/".format(name_without_ext)

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, remote_path)

        # Uncompress the archive on the web server
        run("mkdir -p {}".format(data_path))
        run("tar -xzf {} -C {}".format(remote_path, data_path))

        # Delete the archive from the web server
        run("rm {}".format(remote_path))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current on the web server
        run("ln -s {} /data/web_static/current".format(data_path))

        return True
    except:
        return False
