Mac OS X
========

Homebrew
--------
::

   bash
   ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
   brew doctor

Goodies
-------

Get some stuff. Get OpenCV by first tapping the *science* repo.
Be sure to update.
::
   
   brew install wget scons 
   brew tap science
   brew install opencv
   brew update

Add missing right-ctrl key
--------------------------

Download and install 
`KeyRemap4MacBook <https://pqrs.org/macosx/keyremap4macbook>`_.

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

Emacs over SSH
--------------

To run emacs with XForwarding, we gotta build emacs from source.

See http://stackoverflow.com/questions/22735651/how-to-run-emacs-in-ssh-x-from-linux-to-mac-os-x-with-xforwarding/22736527#22736527.

Get prerequisites, config and make:
::

   brew install libjpeg libtiff
   wget http://ftp.gnu.org/gnu/emacs/emacs-24.3.tar.xz
   tar xf emacs-24.3.tar.xz
   cd emacs-24.3/
   ./configure --with-x --with-gif=no
   make
   make install

Duh
---

#. Switch between different applications with Cmd-Tab
#. Switch between windows of same application with Cmd-`
