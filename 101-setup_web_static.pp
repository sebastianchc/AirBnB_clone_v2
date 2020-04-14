# Set up web server for deployment of web static with puppet
exec { 'Update':
     command => '/usr/bin/apt-get -y update'
}

exec { 'Install':
     require => Exec['Update'],
     command => '/usr/bin/apt-get -y install nginx'
}

exec { 'Shared':
     require => Exec['Install'],
     command => '/bin/mkdir -p /data/web_static/shared/'
}

exec { 'Releases':
     require => Exec['Shared'],
     command => '/bin/mkdir -p /data/web_static/releases/test/'
}

exec { 'Content':
     require => Exec['Releases'],
     command => '/bin/echo "Holberton School" > /data/web_static/releases/test/index.html'
}

exec { 'Symbolic':
     require => Exec['Content'],
     command => '/bin/ln -sf /data/web_static/releases/test/ /data/web_static/current'
}

exec { 'Permissions':
     require => Exec['Symbolic'],
     command => '/bin/chown -R ubuntu:ubuntu /data/'
}

exec { 'Location':
     require     => Exec['Permissions'],
     command     => '/bin/sed -i "38i location /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n" /etc/nginx/sites-enabled/default'
}

exec { 'Restart':
     require => Exec['Location'],
     command => '/usr/sbin/service nginx restart'
}