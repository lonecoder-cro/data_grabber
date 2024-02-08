<<<<<<< HEAD
#! python3
# @Author: Jaedan Willis
# @Company: Official Grasp Technology

import argparse

try:
    from email_extractor import EmailExtractor
    from img_extractor import ImgExtractor
    from num_extractor import NumExtractor
    from wifi_extractor import WifiExtractor
except ImportError as e:
    raise ImportError(str(e))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', type=str,
                        help="""
                        Specified the type of data you want to extract. Types (num,email,wpass,img)
                        Note: imgd only support jpg files for now
                        """, required=True)
    parser.add_argument('-f', '--filename', type=str,
                        help='File you want to extract from')
    parser.add_argument('-u', '--url', type=str,
                        help='A url to a website you want to extract data from')
    parser.add_argument('--timeout', type=float,
                        help='Used with (-u|--url) for javascript wepage loading timeout due to loading javascript files')
    args = parser.parse_args()

    match args.type:
        case "img":
            ImgExtractor(args.filename, args.url)
        case "email":
            EmailExtractor(args.filename, args.url,args.timeout)
        case "num":
            NumExtractor(args.filename, args.url,args.timeout)
        case 'wpass':
            WifiExtractor()
        case _:
            parser.print_usage()

if __name__ == '__main__':
    main()
=======
#! python3
# @Author: Jaedan Willis
# @Company: Official Grasp Technology

import argparse

try:
    from email_extractor import EmailExtractor
    from img_extractor import ImgExtractor
    from num_extractor import NumExtractor
    from wifi_extractor import WifiExtractor
except ImportError as e:
    raise ImportError(str(e))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', type=str,
                        help="""
                        Specified the type of data you want to extract. Types (num,email,wpass,img)
                        Note: imgd only support jpg files for now
                        """, required=True)
    parser.add_argument('-f', '--filename', type=str,
                        help='File you want to extract from')
    parser.add_argument('-u', '--url', type=str,
                        help='A url to a website you want to extract data from')
    parser.add_argument('--timeout', type=float,default=10.0,
                        help='Used with (-u|--url) for javascript wepage loading timeout due to loading javascript files')
    args = parser.parse_args()

    match args.type:
        case "img":
            ImgExtractor(args.filename, args.url)
        case "email":
            EmailExtractor(args.filename, args.url,args.timeout)
        case "num":
            NumExtractor(args.filename, args.url,args.timeout)
        case 'wpass':
            WifiExtractor()
        case _:
            parser.print_usage()

if __name__ == '__main__':
    main()
>>>>>>> 563ec81 (new)
