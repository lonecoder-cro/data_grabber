<<<<<<< HEAD
#! python3
# @Author: Jaedan Willis
# @Company: Official Grasp Technology

import re
import os
import sys
import subprocess

try:
    from web_helper import WebHelper
except ImportError as e:
    raise ImportError(str(e))

class NumExtractor:
    def __init__(self,filename: str = None, url: str = None,timeout:float=0.0):
        if filename:
            self.__extract_from_file(filename)
        elif url:
            self.__extract_from_url(url,timeout)
        else:
            raise ValueError(f'')

    def __extract_from_file(self,filename):
        if not os.path.isfile(filename):
            raise Exception(f'file ({filename}) not found')

        with open(filename, 'r')as infile:
           # for c in infile:
            self.extract(infile.read())

    def __extract_from_url(self, url,timeout):
        webpage = WebHelper.get_page(url,timeout)
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
=======
#! python3
# @Author: Jaedan Willis
# @Company: Official Grasp Technology

import re
import os

try:
    from web_helper import WebHelper
except ImportError as e:
    raise ImportError(str(e))

class NumExtractor:
    def __init__(self,filename: str = None, url: str = None,timeout:float=0.0):
        if filename:
            self.__extract_from_file(filename)
        elif url:
            self.__extract_from_url(url,timeout)
        else:
            raise ValueError(f'')

    def __extract_from_file(self,filename):
        if not os.path.isfile(filename):
            raise Exception(f'file ({filename}) not found')

        with open(filename, 'r')as infile:
           # for c in infile:
            self.extract(infile.read())

    def __extract_from_url(self, url,timeout):
        webpage = WebHelper.get_page(url,timeout)
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
>>>>>>> 563ec81 (new)
