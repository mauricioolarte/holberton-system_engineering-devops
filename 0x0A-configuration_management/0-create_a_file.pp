# this create a file
$mode = 0744
$owner = "www-data"
$group = "www-data"
$str = "I love Puppet"

file {'/tmp/holberton':
  ensure  => present,
  mode    => $mode,
  owner   => $owner,
  group   => $group,
  content => $str,
  }