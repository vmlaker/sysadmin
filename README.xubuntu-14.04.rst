Xubuntu 14.04 on a workstation
==============================

The basics
----------
::

   sudo su -
   apt-get install xfce-goodies xfwm4-themes tcsh tkdiff emacs

Window manager broken
---------------------
If window manager breaks, see 
http://ubuntuforums.org/showthread.php?t=1765417

The fix is to clear the session cache 
and restart the window manager
(use Alt+F2 if needed):
::

   rm -rf ~/.cache/sessions
   xfwm4
   
   
