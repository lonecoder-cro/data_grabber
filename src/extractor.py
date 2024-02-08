#! python3
# @Author: Jaedan Willis
# @Company: Official Grasp Technology

import re
import os
import sys
import argparse
import threading
import ctypes
import subprocess

try:
    import bs4
    import requests
    import requests_html
    from ogt.ogtnet.ogtuseragents import OGTUserAgents
    from ogt.ogtparser.ogtphonenumber import OGTPhoneNumber
except ImportError as e:
    raise ImportError(str(e))

class WebHelper:
    @classmethod
    def get_page(cls,url:str):
        try:
            r = requests.get(url=url, headers={
                             'user-agent': OGTUserAgents.get_user_agents()})
            if r.status_code == 200:
                return cls.__parse(r.content)
            raise Exception(r.status_code)
        except Exception as e:
            raise ValueError(str(e))

    @staticmethod
    def __parse( content:str):
        try:
            return bs4.BeautifulSoup(content, 'lxml').text
        except Exception as e:
            print(str(e))


class EmailExtractor:
    def __init__(self, filename: str = None, url: str = None):
        if filename:
            self.extract_from_file(filename)
        elif url:
            self.extract_from_url(url)
        else:
            raise ValueError(f'')
        # print('\nProcess complete.\n')

    def extract_from_file(self, filename):
        if not os.path.isfile(filename):
            raise Exception(f'file ({filename}) not found')

        with open(filename, 'r')as infile:
            #for c in infile:
            self.extract(infile.read())

    def extract_from_url(self, url):
        webpage = WebHelper.get_page(url)
        self.extract(webpage)

    @staticmethod
    def extract(data: str):
        regex = re.compile(
            r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")
        matches = re.findall(regex, data)

        total: int = 1
        for i in matches:
            print('{}.{}'.format(total, i.lstrip()))
            total += 1


class TeleExtractor:
    def __init__(self,filename: str = None, url: str = None):
        if filename:
            self.extract_from_file(filename)
        elif url:
            self.extract_from_url(url)
        else:
            raise ValueError(f'')
        # print('\nProcess complete.\n')

    def extract_from_file(self,filename):
        if not os.path.isfile(filename):
            raise Exception(f'file ({filename}) not found')

        with open(filename, 'r')as infile:
           # for c in infile:
            self.extract(infile.read())

    def extract_from_url(self, url):
        webpage = WebHelper.get_page(url)
        self.extract(webpage)

    @staticmethod
    def extract(data:str):
        regex = re.compile(r"((1?)(-| ?)(\()?(\d{3})(\)|-| |\)-|\) )?(\d{3})(-| )?(\d{4})|\d{4})")
        matches = re.findall(regex, data)

        total:int = 1
        for i in matches:
            if len(i[0].lstrip()) == 10 or len(i[0].lstrip()) == 12 or len(i[0].lstrip()) == 14:
                print('{}.{}'.format(total, i[0].lstrip()))
                total += 1


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
