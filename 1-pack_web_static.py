#!/usr/bin/python3
"""Script to generate a .tgz archive"""
from fabric.api import local
import tarfile
import re
from datetime import datetime
import os


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
