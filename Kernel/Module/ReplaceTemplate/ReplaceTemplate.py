#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import json
from Kernel.Config.Config import Config

class ReplaceTemplate:
    def ErrorLog():
        print('Quit! Module ReplaceTemplate Error.')
        exit(-1)

    def ReplaceTarget(param, templateKey):
        content = param[templateKey]
        try:
            isRelaceHash = False
            listContent = ''
            if '@@key@@' in content and '@@value@@' in content:
                isRelaceHash = True

            for key,value in param.items():
                if key != templateKey:
                    if isinstance(value, dict) or isinstance(value, list):
                        value = json.dumps(value)
                    elif isinstance(value, int):
                        value = str(value)
                    elif isinstance(value, bool):
                        value = str(value)
                    if isRelaceHash:
                        tempContent = content.replace(f'@@key@@', key)
                        listContent += tempContent.replace(f'@@value@@', value) + '\n'
                    else:
                        content = content.replace(f'@@{key}@@', value)
            if isRelaceHash:
                content = listContent.removesuffix('\n')
        except Exception as e:
            print(f'Error: {e}')
            ReplaceTemplate.ErrorLog()
        return content

    def Traverse(param, frontKey, templateKey):
        if isinstance(param, list):
            isContract = False
            for index in range(len(param)):
                param[index] = ReplaceTemplate.Traverse(param[index], frontKey, templateKey)
                if isinstance(param[index], str):
                    isContract = True
            if isContract == True:
                content = ''
                for value in param:
                    if isinstance(value, dict) or isinstance(value, list):
                        value = json.dumps(list)
                    elif isinstance(value, int):
                        value = str(value)
                    elif isinstance(value, bool):
                        value = str(value)
                    content += value + '\n'
                param = content.removesuffix('\n')
        elif isinstance(param, dict):
            isReplace = False
            for key,value in param.items():
                if isinstance(value, str):
                    if key == templateKey:
                        isReplace = True
                else:
                    param[key] = ReplaceTemplate.Traverse(value, key, templateKey)
            if isReplace == True:
                print(f'{Config.logPrefix}{frontKey}')
                param = ReplaceTemplate.ReplaceTarget(param, templateKey)
        return param

    def DoStart(targetParam, moduleParam):
        templateKey = moduleParam['mod_templateKey'] if 'mod_templateKey' in moduleParam else ''

        targetParam = ReplaceTemplate.Traverse(targetParam, '', templateKey)  
        return targetParam

    def Start(targetParam, moduleParam):
        return ReplaceTemplate.DoStart(targetParam, moduleParam)