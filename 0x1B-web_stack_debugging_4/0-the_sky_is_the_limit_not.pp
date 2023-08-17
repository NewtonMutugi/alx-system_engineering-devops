# Puppet increases the limit of request in the nginx server

# Increase the ULIMIT
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart the nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Exec['fix--for-nginx']
}

