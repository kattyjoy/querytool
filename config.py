# encoding: utf-8
__author__ = "diaoboyu"

import os
#from flaskext.mysql import MySQL
from flask import Flask,request,g,redirect,url_for,render_template,flash,session
from functools import wraps
import time

day = ''
dayindex = 0

SPARK_INFO= {
	'master': '192.168.0.1',
	'port': 7077,
}
#MYSQL_INFO = {
#'host': '192.168.0.5',
#'host': 'localhost',
#'user': 'root',
#'passwd': 'wsn123',
#'db': 'aisdb'
#}
MYSQL_INFO = {
'host': '10.5.0.189',
#'host': 'localhost',
'port':3306,
'user': 'wsn',
'passwd': 'sensor',
'page_size': 10,
'output_path' : 'e:\\output\\'
}
MYSQL_COL_TABLE ={
#    'tablename': 'L1_Ship_Last_Position',
    'tablename': 'ais_small',
    'time': 'Record_Datetime',
    'longitude':'Longitude',
    'latitude':'Latitude',
    'mmsi':'MMSI'
    }
MYSQL_DB_INFO = {
	'querydb': 'ais_dby',
	'tasklogdb':'ais_dby'
}
MYSQL_TASK_INFO={
    'detailtable': 'taskdetail',
    'listtable':'tasklog',
    'taskid':'taskid',
    'source':'source',
    'timestart':'timestart',
    'timeend':'timeend',
    'tp':'tp',
    'pt1':'pt1',
    'pt2':'pt2',
    'mmsi':'mmsi',
    'opformat':'opformat',
    'listid':'id',
    'liststatus':'status',
    'listtaskid':'taskid',
    'listtimestart': 'starttime'
}

SEARCH_NAME_CONFIG={
    'formid':'queryform',
    #array of tuple,[(start,end),(,)...]
    'timeperiods':'timeperiods',
    'pmodetype':'pmodetype',
    #array of tuple ,[(tp,(pt1x,pt1y),(pt2x,pt2y)),....]
    'positions':'positions',
    'harborname':'harborname',
    #'tp':'tp',
    #tuple,(0,0)
    #'pt1':'pt1',
    #tuple,(0,0)
    #'pt2':'pt2',
     #array,[] means not determined
    'shipmmsis':'shipmmsis',
    #array,[] means not determined
    'shipcountries':'shipcountries',
    'database':'database',
    'filetype':'filetype'
}



# init mysql
#mysql = MySQL()


'''

{{dict(config['SEARCH_NAME_CONFIG'])['formid']}}
{{dict(config['SEARCH_NAME_CONFIG'])['timestart']}}
{{dict(config['SEARCH_NAME_CONFIG'])['timeend']}}
{{dict(config['SEARCH_NAME_CONFIG'])['pmodetype']}}
{{dict(config['SEARCH_NAME_CONFIG'])['tp']}}
{{dict(config['SEARCH_NAME_CONFIG'])['pt1']}}
{{dict(config['SEARCH_NAME_CONFIG'])['pt2']}}
{{dict(config['SEARCH_NAME_CONFIG'])['shipmmsis']}}
{{dict(config['SEARCH_NAME_CONFIG'])['shipcountries']}}
{{dict(config['SEARCH_NAME_CONFIG'])['database']}}
{{dict(config['SEARCH_NAME_CONFIG'])['filetype']}}
'''