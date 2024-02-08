#! python3
# @Author: Jaedan Willis
# @Company: Official Grasp Technology

import re
import os
import sys

try:
    from web_helper import WebHelper
except ImportError as e:
    raise ImportError(str(e))

class EmailExtractor:
    def __init__(self, filename: str = None, url: str = None,timeout:float=0.0):
        if filename:
            self.extract_from_file(filename)
        elif url:
            self.extract_from_url(url,timeout)
        else:
            raise ValueError(f'')

    def extract_from_file(self, filename):
        if not os.path.isfile(filename):
            print(f'file ({filename}) not found')
            exit()

        with open(filename, 'r')as infile:
            #for c in infile:
            self.extract(infile.read())

    def extract_from_url(self, url,timeout):
        webpage = WebHelper.get_page(url,timeout)
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
