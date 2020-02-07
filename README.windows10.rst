Windows 10
==========

Step 1
======
Get WSL installed.

WSL (Windows Subsystem for Linux)
---------------------------------
::

   apt install wsl

Mount drives
------------
::

   mkdir /mnt/d
   mount -t drvfs D: /mnt/d -o metadata,uid=1000,gid=1000

``/etc/fstab``
--------------
::

   G:                      /mnt/g   drvfs  metadata,uid=1000,gid=1000 0 0
   
   
