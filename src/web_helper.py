#! python3
# @Author: Jaedan Willis
# @Company: Official Grasp Technology

import urllib.request

try:
    import bs4
    import requests
    from requests_html import HTMLSession,MaxRetries
    from ogt.net.useragent import UserAgents
except ImportError as e:
    raise ImportError(str(e))

class WebHelper:
    @classmethod
    def get_page(cls,url:str,timeout:float=5):
        try:
            session = HTMLSession()
            res = session.get(url)
            if res.status_code == 200:
                res.html.render(timeout=timeout)
                return res.html.text
            print(f'website response with -> {res.status_code}')
            exit()
        except MaxRetries as e:
            print(f'unable to render the page. Try increasing timeout')
            exit()

    @classmethod
    def get_image(cls,url):
        path:str= os.path.join( os.environ.get('temp'), 'OGT-ImDataImageTest.jpg')
        try:
            urllib.request.urlretrieve(url,path)
            urllib.request.urlcleanup()
            return path
        except Exception as e:
            print(str(e))
