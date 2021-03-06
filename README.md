py-lgtv
=======

py-lgtv is a python driver for LG televisions.

Most television models of this manufacturer can be controlled externally using a Serial (RS232) interface.
You'll need to connect the serial port of the television to a serial port of your computer using a null-modem (cross) cable.


Requirements
------------

py-lgtv require [pySerial](http://pyserial.sourceforge.net/) (also called [python-serial](https://packages.debian.org/fr/wheezy/python-serial) on Debian)


Installation
------------

Download the latest source code

    git clone https://github.com/alexismeneses/py-lgtv


To install the module, run the following as root (usually with sudo)

    python setup.py install


Python Library Usage
--------------------

```python
import lgtv

# Choose the serial port which is connected to the RS232 port of your TV
# This may be of the form /dev/ttyUSBx for USB dongles
device = '/dev/ttyS0'

lg = lgtv.LGTV(device)

# Power ON the television
lg.on()

# Set the input source to HDMI1
lg.setsource(lgtv.LG_SOURCE_HDMI1)

# Set the sound to 20%
lg.setsound(20)
```


Command Line Interface
----------------------

You can also use py-lgtv as a CLI tool, driving your TV from the command line or shell script

Print the status of the TV connected to the first USB/serial dongle (ttyUSB0)
```Shell
lgtv --device=/dev/ttyUSB0
```

Change the input source to Digital TV
```Shell
lgtv --device=/dev/ttyS0 source dtv
```

Set the sound to 1%
```Shell
lgtv --device=/dev/ttyS0 sound 1
```

