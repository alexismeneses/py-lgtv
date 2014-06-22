py-lgtv
=======

py-lgtv is a python driver for LG televisions.

Most television models of this manufacturer can be controlled externally using a Serial (RS232) interface.
You'll need to connect the serial port of the television to a serial port of your computer using a null-modem (cross) cable.


Requirements
------------

py-lgtv require [pySerial](http://pyserial.sourceforge.net/) (also called [python-serial](https://packages.debian.org/fr/wheezy/python-serial) on Debian)


Library Usage
-------------

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


