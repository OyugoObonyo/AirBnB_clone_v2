#!/usr/bin/env bash
#Bash script that sets up web server for deployment

#install nginx web server 
apt-get update
apt-get install -y nginx

#create necessary docs and dirs
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Holberton School" >> /data/web_static/releases/test/index.html

#create symbolic link as specified
ln -sf /data/web_static/releases/test/ /data/web_static/current

#set ubuntu as group and user
chown -R ubuntu /data/
chgrp -R ubuntu /data/

#tweak nginx configurations
printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;
        root /var/www/html;
        index index.html index.htm;
        
        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
        }
}" > /etc/nginx/sites-available/default

#Restart nginx for changes to take effect
service nginx restart
