# -*- coding: UTF-8 -*-

import csv
import json
import ast
import re


file = './error.csv'

def ReadCSV():

    errorVidFile = open('./404.json', 'r')
    listError = json.load(errorVidFile)
    print "vid no request num:" + str(len(listError))
    diffList = []

    # Open File CSV
    with open(file, 'r') as File:
        reader = csv.reader(File)
        vidlist = []
        errorDict = {}
        count = 0

        # Read all row in File CSV
        for row in reader:
            count = count + 1

            dictContext = strToDict(row[1], 'context')

            if(dictContext == 'NULL'):
                continue

            dictMalfunction = strToDict(row[6], 'Malfunction')
           
            if dictMalfunction != 'NULL':
                vidlist.append(dictContext['vid'])
                
                dictMalfunction = strToDict(row[6], 'Malfunction')
                print dictMalfunction
            

        print str(count) + '行数据'
        vidlist = list(set(vidlist))
        print len(vidlist)
        
        #list or dict数据写.json文件
        with open('vidlist.json', 'w') as f:
            json.dump(vidlist, f)

        with open('errorDict.json', 'w') as f:
            json.dump(errorDict, f)

        # list取差集
        diffList = list(set(listError).difference(set(vidlist)))
        print 'diff all num: ' +  str(len(diffList))

        with open('diff.json', 'w') as f:
            json.dump(diffList, f)

def strToDict(source, name):
    strRst = ''
    if(source):
        strRst = source

    if strRst == 'NULL' or strRst == 'Col7' or strRst == 'Col2':
        return 'NULL'

    #print("开始打印"+name+"数据\n")
    # 字符串替换
    strRst = strRst.replace('NULL', '""').replace('null', '""').replace('"""', '"\'\'')
    # 字符串转dict结构，literal_eval比较安全
    dictRst = ast.literal_eval(strRst)
    return dictRst

ReadCSV()