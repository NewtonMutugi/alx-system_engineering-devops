# Increases the limit of request in the nginx server

# Increase the ULIMIT
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart the nginx service
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

