Raspberry Pi 2
==============

Setup
-----

#. Download https://www.raspberrypi.org/downloads:
   ::

      wget https://downloads.raspberrypi.org/raspbian_lite_latest
      unzip raspbian_lite_latest
      sudo umount /dev/sdb1 /dev/sdb2
      dd bs=4M if=xxx.img of=/dev/sdb status=progress conv=fsync
   
#. Boot. A message should flash indicating that the filesystem is resized.
   Login with username pi, password raspberry.

#. Check out the system:
   ::

      df -h
      lscpu
      vcgencmd measure_temp
      vcgencmd measure_volts

#. Config:
   ::

      sudo raspi-config
      
Network
-------

1) Enable and start services:
::

   systemctl enable ssh wpa_supplicant
   systemctl start ssh wpa_supplicant
  
2) wpa supplicant:
::

   wpa_cli
   > add_network
   > set_network 0 ssid "<ssid>"
   > set_network 0 psk "<psk>"
   > enable_network 0
   > save_config

Fix network disconnects (from http://raspberrypi.stackexchange.com/a/5341):
::

   sudo cp /etc/ifplugd/action.d/ifupdown /etc/ifplugd/action.d/ifupdown.`date +%Y-%m-%d`
   sudo ln -sf ../../wpa_supplicant/ifupdown.sh /etc/ifplugd/action.d/ifupdown

Disable the ACT LED by adding to ``/boot/config.txt``:
::

   dtparam=act_led_trigger=none
   dtparam=act_led_activelow=off

Disable the PWR LED by adding to ``/boot/config.txt``:
::

   dtparam=pwr_led_trigger=none
   dtparam=pwr_led_activelow=off

Disable the default 100MB swap:
::

   free -h
   ls -la /etc/dphys-swapfile
   sudo swapoff --all
   sudo dphys-swapfile swapoff
   sudo systemctl disable dphys-swapfile
   sudo update-rc.d -f dphys-swapfile remove
   free -h
   sudo rm -rf /var/swap
   
Add swap on USB stick:
::

   sudo fdisk /dev/sda  
   sudo mkswap /dev/sda
   sudo swapon /dev/sda
   free -m
   sudo echo '/dev/sda none swap defaults 0 0' >> /etc/fstab

Reduce power usage by adding a cronjob that checks if it's ON,
and if so, turns it OFF. We do this in a cronjob with small delay,
so that we have some time after booting to disable the control:
::

   MAILTO=""
   * * * * * sleep 20; tvservice -s | grep 'TV is off' ; if [ $? -eq 1 ] ; then tvservice -o ; fi 

Reduce memory usage by Apache HTTPD. Default settings
start two processes of about 222MB each. This can be reduced
to one process of about 145MB by changing the *worker MPM* settings
in file ``/etc/apache2/apache2.conf`` to:
::

   <IfModule mpm_worker_module>
       StartServers          1
       MinSpareThreads       5
       MaxSpareThreads      25 
       ThreadLimit          64
       ThreadsPerChild      15
       MaxClients           50
       MaxRequestsPerChild   0
   </IfModule>

From a post by Vegator at
http://linuxonflash.blogspot.com/2015/02/a-look-at-raspberry-pi-2-performance.html

Stable overclocking:
::

   CPU     Over-   Core    Base
   clock   volt    clock   Clock   CPU : Core      SDRAM   Overv.
   
   1067    +4      533     533     2 : 1           467
   1050    +4      600     150     7 : 4           483     +2
   1000    +2      600     100     5 : 3           500     +4
   1000            500     500     2 : 1           483     +2
    900    +2      600     133     3 : 2           467
    900            450     450     2 : 1           450


config.txt settings:

* `arm_freq` - CPU frequency
* `over_voltage` - CPU/main SoC voltage
* `core_freq` - core clock (L2 cache speed
* `sdram_freq` - SDRAM frequency
* `over_voltage_sdram_p` - voltage for SDRAM physical layer
* `over_voltage_sdram_i` - voltage for I/O
* `over_voltage_sdram_c` - voltage for controller
* `gpu_mem` - RAM dedicated to GPU (total from 1GB available)

For example, 1000 MHz CPU, with stable 483 MHz SDRAM, as well as 256 MB memory reserved for GPU
::

    arm_freq=1000
    over_voltage=0
    core_freq=500
    sdram_freq=483
    over_voltage_sdram_p=0
    over_voltage_sdram_i=0
    over_voltage_sdram_c=0
    gpu_mem=256


Complete table with stability testing results:
::

    CPU     +Volt   Core    SDRAM   +Volt   Stability       Memcpy perf.
                                    p i c   (memtester)     Varied  4K      zcat

    Default:
    900     ?       250     450     0 0 0   OK (slow)       716     1015    2.388s
    Standard overclock (raspi-config "Pi 2" option):
    1000    2       500     500     0 0 0   Fail
    Other settings:
    900     0       450     450     0 0 0   OK              778     1270    2.380s
    900     0       600     467     0 0 0   Almost          804     1431    2.379s
    900     2       600     467     0 0 0   OK (multi-test)
    1000    0       467     467     0 0 0   OK (multi-test) 867     1410    2.146s
    1000    0       500     483     0 0 0   OK (multi-test) 880     1502    2.146s
    1000    0       500     483     2 0 0   OK (multi-test) 878     1502    2.169s
    1000    2       500     500     0 0 0   Almost
    1000    4       500     500     0 0 0   Almost
    1000    0       500     500     2 2 0   Almost
    1000    0       500     500     4 4 0   Almost?
    1000    0       500     500     4 0 0   Fail            886     1415    2.143s
    1000    2       500     500     4 0 0   Fail
    1000    4       500     500     4 4 0   Fail (multi)
    1000    0       500     500     6 6 6   ?
    1000    2       600     467     0 0 0   OK (multi-test) 885     1518    2.145s
    1000    2       600     500     4 0 0   OK (multi-test) 890     1553    2.142s
    1000    2       667     500     4 0 0   Fail (freeze)
    1000    6       667     500     6 0 0   Fail (freeze)
    1050    0       466     466     4 4 4   OK
    1050    0       466     533     4 4 4   Fail
    1050    0       466     533     6 6 6   Fail (bitspr.)
    1050    4       600     450     0 0 0   OK (multi-test) 916     1528    2.045s
    1050    4       600     483     2 0 0   OK (multi-test) 924     1571    2.041s
    1067    6       533     533     6 6 6   Fail
    1067    4       533     533     8 8 0   Fail (bitflip)
    1067    6       533     533     8 8 0   Fail (bitflip)
    1067    6       533     500     4 4 0   Almost
    1067    4       533     466     0 0 0   OK (multi test) 925     1521    2.010s
    1100    0       466     466     0 0 0   Fail (boot)
    1100    4       466     466     0 0 0   OK?
    1100    4       600     467     0 0 0   Fail
    1100    4       500     500     6 6 6   OK?
    1100    4       500     500     6 6 0   OK?
    1100    4       500     500     4 0 0   Almost
    1100    4       500     500     6 0 0   OK?             950     1532    1.950s
    1100    6       500     500     6 0 0   Almost
    1100    4       533     533     6 0 4   Fail            962     1593    1.948s
    1100    4       550     483     0 0 0   OK (multi-test) 944     1549    1.951s
    1133    4       567     466     0 0 0   Almost          974     1578    1.893s
    1133    4       567     467     4 0 0   Almost
    1133    5       567     453     0 0 0   Almost          971     1571    1.896s
    1133    8       567     453     0 0 0   Fail
    1166    4       466     466     0 0 0   Almost          960     1451    1.841s
    1167    4       466     466     2 2 4   Fail
    1166    6       466     466     0 0 0   Fail            962     1451    1.841s
    1167    8       500     500     4 0 0   Fail                            1.839s
    1167    8       500     500     8 8 8   Fail
    1200    8       600     450     4 0 0   Fail


Overclock the 3D block (V3D) of the GPU from 250 MHz to 300 MHz:
::

    force_turbo=1
    avoid_pwm_pll=1
    v3d_freq=300
