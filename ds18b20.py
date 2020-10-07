#
# Copyright (C) 2020 packom.net
# 
# Simple script to read temperatures from DS18B20s on the Raspberry Pi
# For use with the M-Bus Master Hat (DS18B20 variant)
# https://packom.net/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 

#!/usr/bin/python

import os
w1_base = '/sys/bus/w1/devices/'

def find_devices():
  devices = []
  device_paths = os.listdir(w1_base)
  for path in device_paths:
    # Search for DS18B20 devices, whose addresses  start with 28
    if path.startswith('28'):
      devices.append(path)
  return devices

def get_temps(devices):
  temps = []
  for device in devices:
    f = open(w1_base + device + '/w1_slave', 'r')
    lines = f.readlines()
    for line in lines:
      # look for a line ending t=ABCDE
      # A is 10s, B 1s, CDE thousandths
      if line.find('t=') > 0:
        words = line.split(' ')
        ttemp = words[-1]
        temp = ttemp[2:]
        temp = temp[0:2] + '.' + temp[2:-1] + 'C'
        temps.append({"device":device, "temp":temp})
  return temps

def print_temps(temps):
  for temp in temps:
    print("Device: " + temp["device"] + " Temperature: " + temp["temp"])

devices = find_devices()
if len(devices) < 1:
  print('No DS18B20 devices found.\nDo you have \'dtoverlay=w1-gpio\' in your /boot/config.txt file?\n- If not, add it, reboot, then try again.\n- If yes, make sure your DS18B20 devices are properly connected.')
else:
  print('Found devices: ' + ', '.join(devices))
temps = get_temps(devices)
print_temps(temps)
