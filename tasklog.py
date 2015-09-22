# encoding: utf-8
__author__ = "chenzhao"

import os
import MySQLdb
import time
import traceback
import math
from config import MYSQL_INFO,MYSQL_DB_INFO,MYSQL_TASK_INFO
from threading import Thread
from mysqlconn import MySQLConn
class TaskLog:

	day = ''
	dayindex = 0
	@staticmethod
	def getnewtaskid():
		
	    if TaskLog.day == '':
	        TaskLog.day = time.strftime("%Y%m%d_%H%M%S", time.localtime())
	        TaskLog.dayindex += 1
	        return '{0}_{1}'.format(TaskLog.day,TaskLog.dayindex)
	    lastday = time.strptime(TaskLog.day,"%Y%m%d_%H%M%S").tm_mday
	    if time.localtime().tm_mday != lastday:
	        TaskLog.day = time.strftime("%Y%m%d_%H%M%S", time.localtime())
	        TaskLog.dayindex = 1
	    else:
	        TaskLog.dayindex += 1
	    return '{0}_{1}'.format(TaskLog.day, TaskLog.dayindex)
	    
	@staticmethod
	def getcurtaskid():
		return '{0}_{1}'.format(TaskLog.day,TaskLog.dayindex)

	@staticmethod
	def insertlog(source, timestart, timeend, tp, pt1, pt2, mmsi, output):
		conn = MySQLConn(MYSQL_DB_INFO['tasklogdb'])
		cursor = conn.cursor()
		mmsistring = ''
		if mmsi[0] == '0':
			mmsistring = 'ALL'
		else:
			mmsistring = 'FILEPATH'

		start = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(timestart))
		end = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(timeend))
		timenow = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

		taskid = TaskLog.getnewtaskid()
		#print taskid
		sql = 'insert into {9} ({10},{11},{12},{13},{14},{15},{16},{17},{18}) values \
				(\'{0}\',\'{1}\',\'{2}\',\'{3}\',\'{4}\',\'{5}\',\'{6}\',\'{7}\',\'{8}\');' \
				.format(taskid,source,start,end,tp,pt1,pt2,mmsistring,output,MYSQL_TASK_INFO['detailtable'], \
					MYSQL_TASK_INFO['taskid'],MYSQL_TASK_INFO['source'],MYSQL_TASK_INFO['timestart'],\
					MYSQL_TASK_INFO['timeend'],MYSQL_TASK_INFO['tp'],MYSQL_TASK_INFO['pt1'],MYSQL_TASK_INFO['pt2'],\
					MYSQL_TASK_INFO['mmsi'],MYSQL_TASK_INFO['opformat'])
		#print sql
		cursor.execute(sql)

		sql = 'insert into {3} ({4}, {5}, {6}) values \
				(\'{0}\',\'{1}\',\'{2}\');'.format(taskid, 0, timenow,MYSQL_TASK_INFO['listtable'],\
					MYSQL_TASK_INFO['listtaskid'],MYSQL_TASK_INFO['liststatus'], MYSQL_TASK_INFO['listtimestart'])
		#print sql
		cursor.execute(sql)
		cursor.close()
		conn.commit()
		conn.disconnect()
		return taskid
	@staticmethod
	# [startindex,endindex)
	def getlist(startindex,endindex):
		conn = MySQLConn(MYSQL_DB_INFO['tasklogdb'])
		cursor = conn.cursor()

		#for i in range(count / MYSQL_INFO['page_size'] + 1):
		cursor.execute('SELECT {2}, {3}, {4}, {5} FROM {6} ORDER BY {2} DESC\
		 limit {1} offset {0};'.format(startindex, endindex-startindex,MYSQL_TASK_INFO['listid']\
		 	,MYSQL_TASK_INFO['listtaskid'], MYSQL_TASK_INFO['listtimestart'],MYSQL_TASK_INFO['liststatus']\
		 	,MYSQL_TASK_INFO['listtable']))
		result = cursor.fetchall()
		cursor.close();
		conn.disconnect()
		return result
	@staticmethod
	def getdetail(taskid):
		conn = MySQLConn(MYSQL_DB_INFO['tasklogdb'])
		cursor = conn.cursor()
		print 'SELECT * from taskdetail where taskid = "'+taskid+'";'
		#listnum = cursor.execute('SELECT * from taskdetail where taskid = "'+taskid+'";')
		listnum = cursor.execute('SELECT * from {1} where {2} = \'{0}\';'.format(taskid,\
			MYSQL_TASK_INFO['detailtable'],MYSQL_TASK_INFO['taskid']))
		if listnum == 0:
			cursor.close()
			conn.disconnect()
			return "<b>暂无详情</b>"
		item = cursor.fetchall()[0]
		cursor.close()
		conn.disconnect()
		return item
	@staticmethod 
	def gettaskcount():
		conn = MySQLConn(MYSQL_DB_INFO['tasklogdb'])
		cursor = conn.cursor()
		cursor.execute('SELECT count(*) from {0};'.format(MYSQL_TASK_INFO['listtable']))
		count = cursor.fetchall()[0][0]
		return count
