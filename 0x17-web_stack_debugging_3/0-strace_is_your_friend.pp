# This is a sample manifest to show how to use strace to debug a problem

exec { 'fix-apache-issue':
  command     => '/path/to/fix_script.sh',
  refreshonly => true,
}
service { 'apache2':
  ensure => 'running',
  enable => true,
  require => Exec['fix-apache-issue'],
}
