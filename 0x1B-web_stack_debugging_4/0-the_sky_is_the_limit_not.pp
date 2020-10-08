#modifica ulimits in nginx config.

$content = "\"-n 4096\""
exec { 'fix--for-nginx':

  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "sudo sed -i 's/^ULIMIT=.*/ULIMIT=${content}/g' /etc/default/nginx; service nginx restart",
  }
