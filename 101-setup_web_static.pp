# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Ensure necessary directories are created
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '
<html>
  <head></head>
  <body>
    This is a test
  </body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Ensure symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  force  => yes,
}

# Update Nginx configuration (This is a simple way, you might need a more complex approach based on your setup)
file_line { 'nginx_hbnb_static':
  path  => '/etc/nginx/sites-available/default',
  line  => '        location /hbnb_static/ { alias /data/web_static/current/; }',
  match => '^\s*location\s*/hbnb_static/\s*{',
  after => '^\s*location\s*/\s*{',
}

# Ensure Nginx is running and enabled to start on boot
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
