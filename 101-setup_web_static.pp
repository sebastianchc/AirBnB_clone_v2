# Set up web server for deployment of web static with puppet
exec { 'Update' :
     command => '/usr/bin/apt-get -y update'
}

exec { 'Install' :
     require => Exec['Update'],
     command => '/usr/bin/apt-get -y install nginx'
}

exec { 'Test' :
     require => Exec['Install'],
     command => '/bin/mkdir -p /data/web_static/releases/test/'
}

exec { 'Share' :
     require => Exec['Test'],
     command => '/bin/mkdir -p /data/web_static/shared/'
}

exec { 'Content' :
     require => Exec['Share'],
     command => '/bin/echo "Holberton" > /data/web_static/releases/test/index.html'
}

exec { 'Symbolic' :
     require => Exec['Content'],
     command => '/bin/ln -fs /data/web_static/releases/test/ /data/web_static/current'
}

exec { 'Permissions' :
     require => Exec['Symbolic'],
     command => '/bin/chown -R -R ubuntu:ubuntu /data/'
}

exec { 'Location' :
     require: => Exec['Permissions'],
     command => '/bin/sed -i "49i location /hbnb_static {\n\t\talias /data/web_static/current;\n\t}" /etc/nginx/sites-enabled/default'
}

exec { 'Restart' :
     require => Exec['Location'],
     command => '/usr/sbin/service nginx restart'
}