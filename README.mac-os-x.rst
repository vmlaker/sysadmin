Mac OS X
========

Need to ssh into this cute silver paperweight.

Fix X11 error
-------------

To fix `X11 forwarding request failed on channel 0` error:

#. Install `XQuartz <http://xquartz.macosforge.org>`_.
#. Then check file `/etc/sshd_config`. 
   Make sure it has:
   ::
      
      X11Forwarding yes
      XAuthLocation /opt/X11/bin/xauth
      
   Also `/etc/ssh_config`:
   ::

      Host *
      XAuthLocation /opt/X11/bin/xauth
