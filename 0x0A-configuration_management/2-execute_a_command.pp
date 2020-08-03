#kill process whit exec

exec {'kill':
  command  => 'pkill killmenow',
  provider => 'shell',
  }