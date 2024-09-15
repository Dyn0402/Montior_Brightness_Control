#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on September 09 7:41 PM 2024
Created in PyCharm
Created as QGP_Scripts/monitor_brightness_test.py

@author: Dylan Neff, Dylan
"""

from monitorcontrol import get_monitors

def set_brightness(brightness_value):
    monitors = get_monitors()

    for monitor in monitors:
        with monitor:
            print(f'Monitor Pre Luminance {monitor.get_luminance()}')
            monitor.set_luminance(brightness_value)
            print(f"Brightness set to {brightness_value} for monitor: {monitor}")

# Set brightness to 50%
set_brightness(50)