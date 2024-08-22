# Fix Nginx to handle high traffic and reduce failed requests
# Increase the ULIMIT in the Nginx configuration
exec { 'fix-nginx-for-high-traffic':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx to apply changes
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
