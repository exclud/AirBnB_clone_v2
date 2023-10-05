#!/usr/bin/env bash
# Install Nginx if it's not already installed

if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install -y nginx
fi

# Create the specified directories if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
    <head></head>
    <body>
        This is a test
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx to serve content from the created directory
if ! grep -q "hbnb_static" /etc/nginx/sites-available/default; then
    sudo sed -i "s|^\tlocation / {|&\n\t\tlocation /hbnb_static/ {\n\t\t\talias /data/web_static/current/;\n\t\t}|g" /etc/nginx/sites-available/default
fi

# Restart Nginx
sudo service nginx restart
