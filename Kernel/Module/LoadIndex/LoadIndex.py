#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from Kernel.Config.Config import Config
import json
import urllib.request
import os

class LoadIndex:
    def ErrorLog():
        print('Quit! Module LoadIndex Error.')
        exit(-1)
    
    def Download(urlPath):
        print(f'{Config.logPrefix}{urlPath}')
        try:
            result = urllib.request.urlopen(urlPath)
            content = result.read()
            content = json.loads(content)
            print(f'{Config.logPrefix} >> {json.dumps(content)}')
            return content
        except urllib.error.HTTPError as e:
            print('Error: lading fail')
            LoadIndex.ErrorLog()
        return []

    def DoStart(targetParam, moduleParam):
        urlKey = moduleParam['mod_urlKey'] if 'mod_urlKey' in moduleParam else ''
        indexKey = moduleParam['mod_indexKey'] if 'mod_indexKey' in moduleParam else ''
        resultKey = moduleParam['mod_resultKey'] if 'mod_resultKey' in moduleParam else ''

        urlPath = ''
        urlRoot = ''
        if urlKey != '' and urlKey in targetParam:
            urlPath = targetParam[urlKey]
            urlRoot = targetParam[urlKey]
        if indexKey != '' and indexKey in targetParam:
            if urlPath[-1] != '/' and targetParam[indexKey][0] != '/':
                urlPath += '/'+ targetParam[indexKey]
            else:
                urlPath += targetParam[indexKey]
        
        result = LoadIndex.Download(urlPath)
        if not isinstance(result, list):
            print('Error: is not list')
            LoadIndex.ErrorLog()
        else:
            for index in range(len(result)):
                if urlRoot[-1] != '/' and result[index][0] != '/':
                    result[index] = '/' + result[index]
                else:
                    result[index] = result[index]
        
        if resultKey != '' and isinstance(targetParam, dict):
            targetParam[resultKey] = result
        elif resultKey != '':
            targetParam={resultKey:result}
        else:
            targetParam = result

        return targetParam

    def Start(targetParam, moduleParam):
        return LoadIndex.DoStart(targetParam, moduleParam)