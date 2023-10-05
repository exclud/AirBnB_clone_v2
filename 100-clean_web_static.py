#!/usr/bin/python3
from fabric.api import run, env, local
import os
"""Deletes out-of-date archives"""

env.hosts = ['54.157.176.235', '54.144.223.110']
# Optional: Define these if not using default SSH keys and usernames.
# env.user = "your_username"
# env.key_filename = "/path/to/your/ssh/key"


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)

    # First, let's clean up local archives in the 'versions' directory
    with local("ls -t versions", capture=True) as archives:
        archive_list = archives.split("\n")

        # Check if we need to keep only the latest
        if number == 0 or number == 1:
            for archive in archive_list[1:]:
                local("rm -rf versions/{}".format(archive))
        elif number > 1:
            for archive in archive_list[number:]:
                local("rm -rf versions/{}".format(archive))

    # Next, let's clean up archives in the remote servers'
    with cd('/data/web_static/releases'):
        if number == 0 or number == 1:
            result = run("ls -t | grep 'web_static_' | tail -n +2")
            if result:
                for dir_to_remove in result.split("\n"):
                    run("rm -rf {}".format(dir_to_remove))
        elif number > 1:
            result = run
            ("ls -t | grep 'web_static_' | tail -n +{}".format(number + 1))
            if result:
                for dir_to_remove in result.split("\n"):
                    run("rm -rf {}".format(dir_to_remove))
