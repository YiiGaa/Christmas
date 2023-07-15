#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from Kernel.Config.Config import Config
import json
import urllib.request
import os
import time
import random
import shutil

class LoadFile:
    def ErrorLog():
        print('Quit! Module LoadFile Error.')
        exit(-1)
    
    def Download(sourcePath, targetPath, replace):
        print(f'{Config.logPrefix}{sourcePath}')
        print(f'{Config.logPrefix}>> {targetPath}')
        try:
            result = urllib.request.urlopen(sourcePath)    
            checkDir = ''
            for list in targetPath.split('/'):
                checkDir += list
                if checkDir == targetPath:
                    break
                checkDir += '/'
                if os.path.exists(checkDir)==False and os.path.isfile(targetPath)==False:
                    os.mkdir(checkDir, 0o777)
            
            lines = result.readlines()
            targetFile = open(targetPath, 'a', 0o777)
            for line in lines:   
                line = line.decode('utf-8')
                for key,value in replace.items():
                    line = line.replace(key, value)            
                targetFile.write(line)
            targetFile.close()
            
        except urllib.error.HTTPError as e:
            print('Error: lading fail')
            LoadFile.ErrorLog()

    def DoStart(targetParam, moduleParam):
        urlKey = moduleParam['mod_urlKey'] if 'mod_urlKey' in moduleParam else ''
        sourceKey = moduleParam['mod_sourceKey'] if 'mod_sourceKey' in moduleParam else ''
        targetKey = moduleParam['mod_targetKey'] if 'mod_targetKey' in moduleParam else ''
        replaceExtraKey = moduleParam['mod_replaceExtraKey'] if 'mod_replaceExtraKey' in moduleParam else 'Xmas_'
        isJudgeExist = moduleParam['mod_isJudgeExist'] if 'mod_isJudgeExist' in moduleParam else True
        isExistBackup = moduleParam['mod_isExistBackup'] if 'mod_isExistBackup' in moduleParam else True

        targetPath = targetParam[targetKey]
        if targetPath[-1] == '/':
            targetPath = targetPath[0:len(targetPath)-1]

        if os.path.exists(targetPath):
            enter = 'yes'
            if isJudgeExist == True:
                print(f'**warning: {targetPath} already exists, continue generating?')
                cover = 'continue will be covered.' if isExistBackup == False else 'continue will be backed up.'
                print(cover)
                enter = input('yes/no: ')
                if enter != 'y' and enter != 'yes':
                    print('Quit!')
                    exit(-1)
            if (enter == 'y' or enter == 'yes') and os.path.exists(targetPath):
                if isExistBackup == True:
                    renameFile = f'{targetPath}_bak_{time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())}'
                    tryTime = 0
                    while os.path.exists(renameFile) and tryTime < 20:
                        renameFile += '_'+random.randint(0,1000)
                        tryTime+=1
                    if os.path.exists(renameFile)==False:
                        os.rename(targetPath, renameFile)
                else:
                    shutil.rmtree(targetPath)

        replace = {}
        for key,value in targetParam.items():
            if replaceExtraKey not in key:
                replace[key] = value

        if sourceKey != '' and sourceKey in targetParam:
            source = targetParam[sourceKey]
            for value in source:
                sourcePath = targetParam[urlKey]
                targetPath = targetParam[targetKey]
                if sourcePath[-1] != '/' and value[0] != '/':
                    sourcePath += '/'+ value
                else:
                    sourcePath += value
                if targetPath[-1] != '/' and value[0] != '/':
                    targetPath += '/'+ value
                else:
                    targetPath += value
                LoadFile.Download(sourcePath, targetPath, replace)
        return targetParam

    def Start(targetParam, moduleParam):
        return LoadFile.DoStart(targetParam, moduleParam)