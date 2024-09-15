#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on September 15 11:27 PM 2024
Created in PyCharm
Created as Montior_Brightness_Control/MonitorBrightnessControl.py

@author: Dylan Neff, Dylan
"""

import tkinter as tk
from tkinter import ttk
from monitorcontrol import get_monitors


class BrightnessControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Brightness Control")

        self.monitors = get_monitors()
        self.sliders = []

        # Create individual sliders for each monitor
        for idx, monitor in enumerate(self.monitors):
            frame = ttk.Frame(self.root)
            frame.pack(padx=10, pady=5, fill='x')

            label = ttk.Label(frame, text=f'Monitor {idx + 1}')
            label.pack(side='left')

            slider = ttk.Scale(frame, from_=0, to=100, orient='horizontal',
                               command=lambda value, idx=idx: self.set_brightness(idx, int(float(value))))
            slider.set(self.get_current_luminance(monitor))
            slider.pack(side='left', fill='x', expand=True)

            self.sliders.append(slider)

        # Master slider for controlling all monitors
        master_frame = ttk.Frame(self.root)
        master_frame.pack(padx=10, pady=10, fill='x')

        master_label = ttk.Label(master_frame, text="Master Brightness")
        master_label.pack(side='left')

        master_slider = ttk.Scale(master_frame, from_=0, to=100, orient='horizontal', command=self.set_all_brightness)
        master_slider.set(50)  # Set master slider to 50% as default
        master_slider.pack(side='left', fill='x', expand=True)

        self.master_slider = master_slider

    def get_current_luminance(self, monitor):
        with monitor:
            return monitor.get_luminance()

    def set_brightness(self, monitor_idx, brightness_value):
        with self.monitors[monitor_idx] as monitor:
            print(f'Setting Monitor {monitor_idx + 1} brightness to {brightness_value}')
            monitor.set_luminance(brightness_value)

    def set_all_brightness(self, brightness_value):
        brightness_value = int(float(brightness_value))
        print(f'Setting all monitors to brightness {brightness_value}')

        for idx, monitor in enumerate(self.monitors):
            self.sliders[idx].set(brightness_value)
            self.set_brightness(idx, brightness_value)


if __name__ == "__main__":
    root = tk.Tk()
    app = BrightnessControlApp(root)
    root.mainloop()
