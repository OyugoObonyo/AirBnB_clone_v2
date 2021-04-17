#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from fabric.api import env, run, sudo
from datetime import datetime
import os.path

env.user = 'ubuntu'
env.hosts = ['34.73.50.31', '34.73.156.72']


def do_deploy(archive_path):
    """Distributes archives to web servers
       Returns True if successful and false if not
    """
    try:
        if os.path.isfile(archive_path) is False:
            return False
        archFile = archive_path.split('/')[-1]
        archStamp = archFile.split('.')[0]

        # Upload archive to /tmp/ directory
        put(archive_path, '/tmp/{}'.format(archFile))

        # Uncompress archive to /data/web_static/current/ directory
        run('mkdir -p /data/web_static/releases/{}/'.format(archStamp))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archFile, archStamp))

        # Delete archive from web server
        run('rm /tmp/{}'.format(archFile))

        # Delete symbolic link from web server
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'
            .format(archStamp, archStamp))
        run('rm -rf /data/web_static/releases/{}/web_static/'
            .format(archStamp))

        # Create new symbolic link on web server linked to new code version
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archStamp))
    except:
        return False

    return True
