#this scrip install and cofigure a NGINX web server.

exec {'update linux':
  command  => '-y update',
  provider => 'apt-get',
  }

exec {'install nginx':
  command  => '-y install nginx',
  provider => 'apt-get',
  }

exec {'start server':
  command  => 'nginx start',
  provider => 'service',
  }

exec {'kill':
  command  => 'pkill killmenow',
  provider => 'shell',
  }

file-line {'add text to index.html':
  ensure => present,
  path   => '/var/www/html/index.nginx-debian.html',
  line   => 'Holberton School',
  }

file-line {'add redirect':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'server_name _;',
  line   => '\n\t\tlocation /redirect_me {\n\treturn 301 https://www.youtube.com;\n\t}',

  }

exec {'restar server':
  command  => 'nginx restar',
  provider => 'service',
  }








#sudo apt-get -y update
#sudo apt-get -y install nginx
#sudo service nginx start

#sudo echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html


#set_301="location /redirect_me {\n\treturn 301 https://www.youtube.com;\n\t}"
#sudo sed -i "/server_name _/a$set_301" /etc/nginx/sites-enabled/default
#sudo service nginx restart