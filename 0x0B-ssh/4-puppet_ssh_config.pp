#this file add lines
file_line {'turn of password auth':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication',
  }

file_line {'turn of password auth':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/holberton',
  }
