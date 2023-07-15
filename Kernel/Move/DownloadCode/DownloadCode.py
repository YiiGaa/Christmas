#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from Kernel.Module.Module import Module

class DownloadCode:
    def DoStart(targetParam, configParam):
        print('STEP::Get File List')
        targetParam = Module.Start('LoadIndex', targetParam, {
            'mod_urlKey':'Xmas_url',
            'mod_indexKey':'Xmas_index',
            'mod_resultKey':'Xmas_source'
        })

        print('STEP::Download Files')
        targetParam = Module.Start('LoadFile', targetParam, {
            'mod_urlKey':'Xmas_url',
            'mod_sourceKey':'Xmas_source',
            'mod_targetKey':'Xmas_target',
            'mod_replaceExtraKey':'Xmas_',
            'mod_isJudgeExist':configParam['isJudgeExist'],
            'mod_isExistBackup':configParam['isExistBackup']
        })

    def Start(targetParam, configParam):
        DownloadCode.DoStart(targetParam, configParam)
        print('')
        print('SUCCESS')