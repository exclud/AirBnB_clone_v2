# Ensure the apt module is present in your Puppet setup
class { 'apt':
  update => {
    frequency => 'daily',
  },
}

# Ensure the nginx package is installed
package { 'nginx':
  ensure  => installed,
  require => Class['apt::update'],
}

# Create the necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create the test index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  content => "<html>
<head></head>
<body>
    This is a test
</body>
</html>\n",
}

# Ensure symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  force  => true, # This ensures that if the link exists it gets overwritten
}

# Update Nginx to serve content from the created directory
file_line { 'update_nginx_for_hbnb_static':
  path => '/etc/nginx/sites-available/default',
  line => "\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}",
  match => '^\tlocation / {',
  after => '^\tlocation / {',
  require => Package['nginx'],
  notify => Service['nginx'],
}

# Ensure the nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}
