Ubuntu 14.04 on AWS
===================

Get yer environment
-------------------
::

   sudo su -
   apt-get update
   apt-get upgrade
   apt-get install git tcsh emacs

Install dotfiles (for root and user)
------------------------------------
::
   
   cd
   git clone --recursive https://github.com/vmlaker/dotfiles ~/.dotfiles
   cd ~/.dotfiles
   python create.py
   exit

   cd
   git clone --recursive https://github.com/vmlaker/dotfiles ~/.dotfiles
   cd ~/.dotfiles
   python create.py

Change the login shells
-----------------------
::

   sudo su -
   usermod -s /usr/bin/tcsh ubuntu
   usermod -s /usr/bin/tcsh root
   exit
 
