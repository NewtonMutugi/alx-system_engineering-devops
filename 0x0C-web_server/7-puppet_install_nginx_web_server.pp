# Install nginx using puppet

exec { 'server configuration':
  provide => shell,
  command  => 'sudo apt-get -y update; sudo apt-get -y install nginx; echo "Hello World" > /var/www/html/index.html; sudo sed -i "/server_name _;/a location /redirect_me {\\n\\treturn 301 https://google.com;\\n\\t}\\n" /etc/nginx/sites-available/default; sudo service nginx restart'
}
