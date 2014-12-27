CentOS 7
========

Misc:
::

   sudo su
   yum install -y emacs tcsh git xauth net-tools ntp unzip zip gparted


Install `EPEL <https://fedoraproject.org/wiki/EPEL>`_ repo:
::

   yum install -y epel-release

For a server setup, install fail2ban:
::

   yum install -y fail2ban
   cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
   emacs -nw /etc/fail2ban/jail.local
   systemctl enable fail2ban
   systemctl start fail2ban
   systemctl status fail2ban
   
Dotfiles for root user
----------------------
::

   cd
   git clone --recursive https://github.com/vmlaker/dotfiles .dotfiles
   cd .dotfiles
   python create.py
   usermod -s /usr/bin/tcsh root
