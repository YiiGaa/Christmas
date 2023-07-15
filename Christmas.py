#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
    Christmas v2.0
    More Detail: https://github.com/YiiGaa/Christmas
    official: https://stoprefactoring.com
    Designed by Daniel.Leung
'''

import sys
sys.dont_write_bytecode = True
from Kernel.Move.Move import Move

if __name__ == '__main__':
    print('Hi, I am Christmas v2.0')
    print('More Detail: https://github.com/YiiGaa/Christmas')
    print('official: https://stoprefactoring.com')
    print('')

    if not (sys.version_info.major >= 3 and sys.version_info.minor >= 9):
        print('Error! Require python 3.9 or above.')
        print('Current: '+sys.version)
        exit(-1)
    
    if len(sys.argv)>1:
        action = sys.argv[1]
        setting = []
        for list in sys.argv[2:]:
            setting.append(list)
        Move.Start(action, setting)
    else:
        print("Please input function parameters.")
        print("Like: python3 Christmas.py Input/GenCode/xxx")
        print("Input/GenCode/xxx is function parameters.")
        sys.exit(-1)
    sys.exit(0)