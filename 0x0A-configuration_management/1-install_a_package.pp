# Puppet manifest to install Flask 2.1.0 and compatible Werkzeug
package { 'werkzeug':
  ensure   => '2.0.1',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug'],
}
