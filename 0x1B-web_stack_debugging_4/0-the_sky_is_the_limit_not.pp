#modifica ulimits in nginx config.

$content = "\"-n 4096\""
exec { '/etc/default/nginx':

  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "sudo sed -i 's/^ULIMIT=.*/ULIMIT=${content}/g' /etc/default/nginx",
  }

exec { 'nginx restart':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => 'service nginx restart',
  }
