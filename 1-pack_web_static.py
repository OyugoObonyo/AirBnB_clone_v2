#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder of the AirBnB Clone repo,
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates .tgz archive from the contents of /web_static
       returns archive's path if successful and None if not
    """
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    filePath = 'versions/web_static_{}.tgz'.format(now)

    local('mkdir -p versions/')
    createArchive = local('tar -cvzf {} web_static/'.format(filePath))

    if createArchive.succeeded:
        return archive_path
    return None
