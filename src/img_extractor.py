#! python3
# @Author: Jaedan Willis
# @Company: Official Grasp Technology

import os
import sys

try:
    from PIL import Image
    from PIL.ExifTags import TAGS
    from web_helper import WebHelper
except ImportError as e:
    raise ImportError(str(e))

class ImgExtractor(object):
    def __init__(self, filename: str = None, url: str = None):
        if filename:
            self.extract_from_file(filename)
        elif url:
            self.extract_from_url(url)
        else:
            raise ValueError(f'')

    def extract_from_url(self,url):
        img_path = WebHelper.get_image(url)
        try:
            image = Image.open(img_path)
            metadata = image._getexif()
            if metadata:
                for k, v in _info.items():
                    tagname = TAGS.get(k, k)
                    self.metadata[tagname] = v
                    print(f'\t{str(tagname)} : {str(v)}')
            else:
                print('no metadata found' )
        except Exception as e:
            print(str(e))


    def extract_from_file(self,filename):
        if not os.path.isfile(filename):
            print('file %s not found' %  (filename))
            exit()

        trash, extention = os.path.splitext(filename)
        extention = extention.lower()

        if extention.endswith(('.jpg', '.jpeg')):
            image=None
            try:
                image = Image.open(filename)
            except OSError:
                print(f'fail to open file ({filename})')
                exit()

            metadata = image._getexif()
            if metadata:
                for k, v in metadata.items():
                    tagname = TAGS.get(k, k)
                    print(f'{str(tagname)}: {str(v)}')
            else:
                print('no metadata found')
        else:
            print('only .jpg extension alone or supported')
