Red Hat Enterprise Linux 6
==========================

EPEL repo
---------
::

   wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
   rpm -Uvh epel-release-6*.rpm

fail2ban
--------
::

   yum install -y fail2ban

   cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
   sed -i s:'ignoreip = 127.0.0.1/8':'ignoreip = 127.0.0.1/8 my.own.static.ip':g /etc/fail2ban/jail.local

   service fail2ban restart

