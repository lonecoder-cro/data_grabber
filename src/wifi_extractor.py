#! python3
# @Author: Jaedan Willis
# @Company: Official Grasp Technology

import os
import sys
import subprocess

class WifiExtractor:
    def __init__(self):
        net_info = subprocess.check_output(
                ['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        net_info = [i.split(':')[1][1:-1]
                    for i in net_info if 'All User Profile' in i]

        for i,v in enumerate(net_info):
            try:
                result = subprocess.check_output(
                    ['netsh', 'wlan', 'show', 'profile', v, 'key', '=', 'clear']).decode('utf-8').split('\n')
                result = [b.split(':')[1][1:-1]for b in result if 'Key Content' in b]
                print('{}.{:<30} | {:>30}'.format(i,v, result[0]) + '\n')
            except IndexError:
                pass
