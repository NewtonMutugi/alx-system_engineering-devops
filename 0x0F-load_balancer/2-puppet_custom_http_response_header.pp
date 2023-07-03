# Automate the task of creating a custom HTTP header response, but with Puppet.

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create directories
file { '/etc/nginx/html':
  ensure => directory,
}

# Create and write content to the index.html file
file { '/etc/nginx/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Configure Nginx custom HTTP response header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      root /etc/nginx/html;
      index index.html index.htm;

      location /redirect_me {
        return 301 http://youtube.com/UCw4X_zayaSiuVYcqWpiaSWw;
      }

      error_page 404 /404.html;
      location /404 {
        root /etc/nginx/html;
        internal;
      }

      add_header X-Served-By $hostname;
    }
  ",
  notify  => Service['nginx'],
}

# Enable and restart Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
