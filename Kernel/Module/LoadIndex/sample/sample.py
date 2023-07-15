#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
sys.path.append('../../../../')
sys.dont_write_bytecode = True
from Kernel.Module.LoadIndex.LoadIndex import LoadIndex

if __name__ == '__main__':
    targetParam = {
        "Xmas_url":"https://stoprefactoring.com/data/module/Header",
        "Xmas_index":"/Load.json"
    }

    targetParam = LoadIndex.Start(targetParam, {
        'mod_urlKey':'Xmas_url',
        'mod_indexKey':'Xmas_index',
        'mod_resultKey':'Xmas_source'
    })

    print(targetParam)