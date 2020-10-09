virtualbox
==========
For running Ubuntu guest on a Windows host:

Settings
--------
* General->Advanced->Shared Clipboard: Bidirectional
* System->Motherboard->Chipset: PIIX3
* System->Motherboard->Pointing Device: USB Tablet
* System->Motherboard->Extended Features: Enable I/O APIC (others unchecked)
* System->Acceleration->KVM & Enable Nested Paging
* Display->Graphics Controller: VMSVGA
* Display->Acceleration: Leave unchecked
* Audio->Host Audio Driver: Windows DirectSound
* Audio->Audio Controller: ICH AC97
* Audio->Extended Features: Both checked
* Shared Folders: Add host drive...

Add user to group
-----------------
::

   usermod -a -G vboxsf <username>

Reduce VDI file size (windows host, linux guest)
------------------------------------------------
From https://superuser.com/a/529183/225901:

1. Nullify free space
   ::

      dd if=/dev/zero of=/var/tmp/bigemptyfile bs=4096k ; rm /var/tmp/bigemptyfile

2. Shutdown VM

3. Run ``modifymedium`` on host:
   ::

      VBoxManage.exe modifymedium --compact C:\path\to\thedisk.vdi
