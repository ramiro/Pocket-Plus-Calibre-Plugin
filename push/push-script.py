#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
python push-script.py /Users/magnus/Library/Mobile\ Documents/iCloud~is~workflow~my~workflows/Documents
"""
import argparse
import glob
import os
import shutil

def get_parser():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    #parser.add_argument('-', "--", help="", default="")
    parser.add_argument("-d", "--dev",
                        action="store_true", help="don't remove files")
    parser.add_argument("-v", "--verbose",
                        action="store_true", help="be verbose")
    parser.add_argument("path", help="", default="") # nargs='+')
    parser.add_argument("script", help="", default="") # nargs='+')
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    path = args.path + '/*'
    if len(glob.glob(path)):
        os.system("osascript -e 'display notification \"Push Pocket\" with title \"Pocket+\"'")
        os.system('source ' + args.script)
    if not args.dev:
        # fetch file list again to remove all files there
        for f in glob.glob(path):
            os.remove(f)
