CentOS 6.5
==========

First things first
:
::

   yum groupinstall "Development tools"

Python
(as per http://toomuchdata.com/2014/02/16/how-to-install-python-on-centos)
:
::

   yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel
   wget http://python.org/ftp/python/2.7.6/Python-2.7.6.tar.xz
   tar xf Python-2.7.6.tar.xz
   cd Python-2.7.6
   ./configure --prefix=/usr/local --enable-unicode=ucs4 --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
   make && make altinstall
   
Git
(as per http://git-scm.com/book/en/Getting-Started-Installing-Git)
:
::

   yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel
   yum install perl-ExtUtils-MakeMaker
   git clone https://github.com/git/git
   cd git
   make prefix=/usr/local all
   sudo make prefix=/usr/local install

