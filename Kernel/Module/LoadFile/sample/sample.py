#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
sys.path.append('../../../../')
sys.dont_write_bytecode = True
from Kernel.Module.LoadFile.LoadFile import LoadFile

if __name__ == '__main__':
    targetParam = {
        'Xmas_url':'https://stoprefactoring.com/data/module/Header',
        'Xmas_target':'./test',
        'Xmas_source': [
            'Header.html', 
            'Header.css', 
            'Header.js', 
            'test/logo.svg'
        ],
        'control-start':'123'
    }

    targetParam = LoadFile.Start(targetParam, {
        'mod_urlKey':'Xmas_url',
        'mod_sourceKey':'Xmas_source',
        'mod_targetKey':'Xmas_target',
        'mod_replaceExtraKey':'Xmas_',
        'mod_isJudgeExist':False,
        'mod_isExistBackup':False
    })

    print(targetParam)