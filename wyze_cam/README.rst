Wyze Cam V2
===========
Download the custom firmware from
`<https://github.com/EliasKotlyar/Xiaomi-Dafang-Hacks>`_:
::

   git clone git@github.com:/EliasKotlyar/Xiaomi-Dafang-Hacks.git

Find your SD card's device:
::

   lsblk

Delete existing partitions and create one FAT32 partition:
::

   sudo fdisk /dev/mmcblk2

Format the new partition:
::

   sudo mkfs.fat /dev/mmcblk2p1
   

