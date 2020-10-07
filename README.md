# hat_ds18b20

Simple python script which queries DS18B20 temperature sensors attached to a Raspberry Pi.

Designed for use with the M-Bus Master Hat (DS18B20 variant).  See https://packom.net/ for more about the M-Bus Master Hat.

To run first of all add this to your /boot/config.txt:

```
dtoverlay=w1-gpio
```

And reboot.

Then clone this repo and run the script:

```
git clone https://github.com/packom/hat_ds18b20
cd hat_ds18b20
python ds18b20.py
```