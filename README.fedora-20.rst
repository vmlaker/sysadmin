Fedora 20
=========

YUM stuff
---------
::

   yum groupinstall "Development tools"
   yum install -y emacs git firefox python-pip 

Python stuff
------------
:: 

   pip install restview

Google Chrome
-------------

As per http://www.if-not-true-then-false.com/2010/install-google-chrome-with-yum-on-fedora-red-hat-rhel

Add to `/etc/yum.repos.d/google-chrome.repo`

32-bit:
::

   [google-chrome]
   name=google-chrome - 32-bit
   baseurl=http://dl.google.com/linux/chrome/rpm/stable/i386
   enabled=1
   gpgcheck=1
   gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub

64-bit:
::

   [google-chrome]
   name=google-chrome - 64-bit
   baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
   enabled=1
   gpgcheck=1
   gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub

Then, as root:
::

   yum install google-chrome-stable google-chrome-beta
