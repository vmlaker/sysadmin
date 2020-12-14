Wyze Cam V2
===========
Get the software
----------------
Download the custom firmware from `<https://github.com/EliasKotlyar/Xiaomi-Dafang-Hacks>`_:
::

   git clone git@github.com:/EliasKotlyar/Xiaomi-Dafang-Hacks.git
   
Prepare the bootloader SD card
------------------------------
Find your SD card's device:
::

   lsblk

Delete existing partitions and create one FAT32 partition:
::

   sudo fdisk /dev/mmcblk2

Format the new partition:
::

   sudo mkfs.fat /dev/mmcblk2p1

Copy custom firmware (CFW) to the SD card:
::

   cp Xiaomi-Dafang-Hacks/hacks/cfw/wyzecam_v2/cfw-1.1.bin /media/username/sdcard_id/demo.bin

Install the bootloader SD card
------------------------------
Remove power cable.
Insert SD card.
Hold down the setup button.
Plug in power cable.
Observe the initial amber light.
After five seconds, observe the light turn blue.
After five more seconds, release setup button.
After 30 more seconds, observe the following sequence of events occur within about five secons:
   Light turns amber.
   Camera clicks.
   Light turns blue.
   LIght turns amber, and stays.
Unplug camera.
Remove SD card.
Plug in camera.
Audible click and amber light.
After five seconds, light turns blue.
After 30 seconds, light turns amber.

Install the CFW
---------------
::

   rsync -av Xiaomi-Dafang-Hacks/firmware_mod/* /media/username/sdcard_id/


SSH into camera
---------------
ssh root@<hostname>  # Password=ismart12
