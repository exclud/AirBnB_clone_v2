#!/usr/bin/python3
"""Script to generate a .tgz archive and deploy it to servers"""
from fabric.api import local, run, put, env
import datetime
import os

env.hosts = ['54.157.176.235', '54.144.223.110']  # updated server IPs

# Optional: Define these if not using default SSH keys and usernames.
# env.user = "your_username"
# env.key_filename = "/path/to/your/ssh/key"


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""

    # Ensure the versions directory exists
    if not os.path.exists('versions'):
        local('mkdir -p versions')

    # Create a filename based on current datetime
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_{}.tgz'.format(timestamp)

    # Use the tar command to generate the .tgz
    archive_command = 'tar -czvf {} web_static'.format(archive_path)
    if local(archive_command).succeeded:
        return archive_path
    else:
        return None


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
