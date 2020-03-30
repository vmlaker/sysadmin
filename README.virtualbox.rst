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
