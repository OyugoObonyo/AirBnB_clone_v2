#!/usr/bin/env bash
#Bash script that sets up web server for deployment

apt-get update
apt install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Holberton School" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm;
        add_header X-Served-By $HOSTNAME;
        
        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
        }
}" > /etc/nginx/sites-available/default

service nginx restart
