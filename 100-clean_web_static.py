#!/usr/bin/python3
from fabric.api import *
from fabric.state import commands, connections
import os.path
"""Deletes out-of-date archives"""

env.hosts = ["54.157.176.235", "54.144.223.110"]  # updated server IPs

# Optional: Define these if not using default SSH keys and usernames.
env.user = 'ubuntu'
env.key_filename = "/home/shammah/.ssh/id_rsa"



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
# def do_clean(number=0):
#     """deletes out-of-date archives"""
#     local('ls -t ~/AirBnB_Clone_V2/versions/').split()
#     with cd("/data/web_static/releases"):
#         target_R = sudo("ls -t .").split()
#     paths = "/data/web_static/releases"
#     number = int(number)
#     if number == 0:
#         num = 1
#     else:
#         num = number
#     if len(target_R) > 0:
#         if len(target) == number or len(target) == 0:
#             pass
#         else:
#             cl = target[num:]
#             for i in range(len(cl)):
#                 local('rm -f ~/AirBnB_Clone_V2/versions/{}'.format(target[-1]))
#         rem = target_R[num:]
#         for j in range(len(rem)):
#             sudo('rm -rf {}/{}'.format(paths, rem[-1].strip(".tgz")))
#     else:
#         pass
