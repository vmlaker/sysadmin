sysadmin
========

Running OSs and stuff.

* `CentOS 6.5 <README.centos-6.5.rst>`_
* `Fedora 20 <README.fedora-20.rst>`_
* `Ubuntu 14.04 <README.ubuntu-14.04.rst>`_
* `Xubuntu 14.04 <README.xubuntu-14.04.rst>`_
* `Mac OS X <README.mac-os-x.rst>`_

yum
---
::

   yum install `cat yum.fedora-20.txt`


XML
---
Strip illegal characters from XML.

StatSVN for example: If during ``java -jar statsvn.jar...`` command, the parsing fails with error like,

``svn log: An invalid XML character (Unicode: 0x10) was found in the element content of the document``

you may consider stripping the illegal characters from the XML logfile:

::

   python clean_svn_xml.py logfile.log logfile_clean.log

