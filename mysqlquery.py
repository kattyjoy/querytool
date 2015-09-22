# encoding: utf-8
__author__ = "chenzhao"

import os
import MySQLdb
import time
import traceback
import math
from config import MYSQL_INFO, MYSQL_COL_TABLE,MYSQL_DB_INFO
import callnglat
from search import Country

from threading import Thread
from mysqlconn import MySQLConn
class mysqlQuery(Thread):
	latcolrad = '(RADIANS('+MYSQL_COL_TABLE['latitude'] + ' / 600000))'
	loncolrad = '(RADIANS('+MYSQL_COL_TABLE['longitude'] + ' / 600000))'
	"""docstring for mysqlQuery"""
#	 def __init__(self,timestart='', timeend='', tp=0, pt1=(0,0), pt2=(0,0), mmsi=['0'],out="csv"):
	'''
		timelist: list[(start,end)] timestamp string
		positionlist: dict['tp':int{0,1,2},'pt1':tuple(float,float),'pt2':tuple(float,float)]
		mmsilist: list[string]
		output:{'csv','text'}
	'''
	def __init__(self,timelist,positionlist,mmsilist,countrylist,output,taskid):
		super(mysqlQuery, self).__init__()
		print 'start connect init'
		self.queryconn = MySQLConn(MYSQL_DB_INFO['querydb'])
		self.timelist = timelist
		self.positionlist = positionlist
		self.mmsilist = mmsilist
		self.countrylist = countrylist
		self.output = output
		self.taskid = taskid
		print 'connect success'
	def query(self):
		print 'function query(self,sql)'
#		self.mysqlconn.close()
		self.queryconn.keepconn()
		sql = mysqlQuery.makeupsql(timelist=self.timelist,positionlist=self.positionlist,mmsilist=self.mmsilist,countrylist=self.countrylist)
		sql += mysqlQuery.makeupoutput(filetype=self.output,filename=self.taskid)
		print 'execute ['+sql+']'
#		cur = self.queryconn.cursor()		
#		result = cur.execute(sql)
#		cur.close()
		print "end query"
		return
		'''
		cur = self.queryconn.conn.cursor()
		#cur.close()
		print 'execute ['+sql+']'
		start = time.time()
		result = cur.execute(sql)
		end = time.time()
		duration = end-start
		print 'execute time: '+str(duration)+'ms'
		start = time.time()
		re = cur.fetchall()
		end = time.time()
		duration = end-start
		print 'fetchall time: '+str(duration)+'ms'
		cur.close()
		index = 0
		for r in re:
			print '======='+str(index)+'========'
			si = 0
			for i in r:
				print str(si)+':  ['+str(i)+']'
				si = si+1
			index = index+1
		print 'end query'
		return re
'''
	@staticmethod
	def makeupsql(timelist=[],positionlist=[],mmsilist=[],countrylist=[]):
		'''
		args:
		timestart : time string
		timeend : time string
		type: number, 0,1,2
		pt1: tuple (,)
		pt2: tuple (,)
		mmsi: string 0 or other
		'''
		sql = 'SELECT * FROM '+MYSQL_COL_TABLE['tablename']+' WHERE '
		sql += "("
		for t in timelist:
			print t
			sql += mysqlQuery.makeuptime(t[0],t[1]) + ' OR '
		if sql[-4:] == ' OR ':
			sql = sql[:-4]
			sql += ")"
			sql +=' AND '
		if sql[-1] == "(":
			sql = sql[:-1]
		print 'time :' +sql
#		sql += mysqlQuery.makeuptime(timestart,timeend)
		sql += "("
		for p in positionlist:
			sql += mysqlQuery.makeupposition(p['tp'],p['pt1'],p['pt2']) + ' OR '
		if sql[-4:] == ' OR ':
			sql = sql[:-4]
			sql += ")"
			sql +=' AND '
		if sql[-1] == "(":
			sql = sql[:-1]
		#sql += mysqlQuery.makeupposition(tp,pt1,pt2)
		
		print 'position :' +sql

		sql += "("
		tmp = mysqlQuery.makeupmmsi(mmsilist)
		if tmp != '':
			sql += tmp + ') AND '
		
		if sql[-1] == "(":
			sql = sql[:-1]
		print 'mmsi :' +sql

		sql += '('
		for country in countrylist:
			sql += mysqlQuery.makeupcountry(country) + ' OR '
		if sql[-4:] == ' OR ':
			sql = sql[:-4]
			sql += ')'
		if sql[-1] == "(":
			sql = sql[:-1]


#		for c in countrylist:
#			sql += mysqlQuery.makeupcountry(c) + ' OR '
		
		if sql[-4:] == ' OR ':
			sql = sql[:-4]
		if sql[-5:] == ' AND ':
			sql = sql[:-5]
		if sql[-6:] == 'WHERE ':
			sql = sql[:-6]
		
#		tmp = mysqlQuery.makeupmmsi(mmsi)
#		if tmp != '':
#			sql +=' AND '+tmp
		


		print 'sql :' + sql
		return sql
	@staticmethod
	def makeuptime(timestart,timeend):
		return '('+MYSQL_COL_TABLE['time'] +' >= '+timestart +' AND '+MYSQL_COL_TABLE['time'] +' <= '+timeend+')'
	@staticmethod
	def makeupposition(tp,pair1,pair2):
		sql = '('
		if tp == 2:
			print 'position type is 2'
			#0
			maxup = callnglat.getdespoint(pair1[0],pair1[1],0,pair2[0])[1]
			#90
			maxright = callnglat.getdespoint(pair1[0],pair1[1],90,pair2[0])[0]
			#180
			maxdown = callnglat.getdespoint(pair1[0],pair1[1],180,pair2[0])[1]
			#-90
			maxleft = callnglat.getdespoint(pair1[0],pair1[1],-90,pair2[0])[0]
			sql = MYSQL_COL_TABLE['latitude'] +' <= ' +mysqlQuery.revertdegree(maxup)+ ' AND '\
				  + MYSQL_COL_TABLE['latitude'] +' >= ' +mysqlQuery.revertdegree(maxdown)+ ' AND '
			if maxleft <= maxright:
				sql+= MYSQL_COL_TABLE['longitude'] + ' >= ' + mysqlQuery.revertdegree(maxleft)+ ' AND '\
				  + MYSQL_COL_TABLE['longitude'] + ' <= ' +mysqlQuery.revertdegree(maxright)
			else:
				sql += '(( ' + MYSQL_COL_TABLE['longitude'] + ' >= ' +mysqlQuery.revertdegree(maxleft) + ' AND '\
					   +MYSQL_COL_TABLE['longitude'] +' <= '+mysqlQuery.revertdegree(180)+' ) OR ( '\
					   +MYSQL_COL_TABLE['longitude'] + ' >= ' + mysqlQuery.revertdegree(-180) + ' AND '\
					   +MYSQL_COL_TABLE['longitude'] + ' <= ' + mysqlQuery.revertdegree(maxright)+'))'
			sql += ' AND ('+ mysqlQuery.makeupdistance(str(math.radians(pair1[0])),str(math.radians(pair1[1]))) + ' <= '+ str(pair2[0])+")"
			return sql
		if tp == 1:
			print 'position type is 1'
		if tp == 0:
			print 'position type is 0'
			pair2 = callnglat.getlowerrightpoint(pair1[0],pair1[1],pair2[0],pair2[1])
		sql = MYSQL_COL_TABLE['latitude'] +' <= ' +mysqlQuery.revertdegree(pair1[1])+ ' AND '\
				  + MYSQL_COL_TABLE['latitude'] +' >= ' +mysqlQuery.revertdegree(pair2[1])+ ' AND '
		if pair1[0] <= pair2[0]:
			sql+= MYSQL_COL_TABLE['longitude'] + ' >= ' + mysqlQuery.revertdegree(pair1[0])+ ' AND '\
				  + MYSQL_COL_TABLE['longitude'] + ' <= ' +mysqlQuery.revertdegree(pair2[0])
		else:
			sql += '( ( ' + MYSQL_COL_TABLE['longitude'] + ' >= ' +mysqlQuery.revertdegree(pair1[0]) + ' AND '\
					   +MYSQL_COL_TABLE['longitude'] +' <= '+mysqlQuery.revertdegree(180)+' ) OR ( '\
					   +MYSQL_COL_TABLE['longitude'] + ' >= ' + mysqlQuery.revertdegree(-180) + ' AND '\
					   +MYSQL_COL_TABLE['longitude'] + ' <= ' + mysqlQuery.revertdegree(pair2[0])+') )'
		
		sql += ')'
		return sql
	@staticmethod
	def makeupmmsi(mmsilist):
		sql = "("
		for m in mmsilist:
			if m != "0":
				sql += "( "+MYSQL_COL_TABLE['mmsi'] +' = '+m+" )  OR "
		if sql != "(" and sql[-4:]==" OR ":
			sql = sql[:-4]
		if sql == "(":
			return ""
		sql += ")"
		return sql
			
			
	@staticmethod
	def makeupcountry(country):
		countrycodes = Country.dmmsi[country]
		sql = ""
		for code in countrycodes:
			sql += " ("+MYSQL_COL_TABLE['mmsi'] + " LIKE '"+code+"%') OR "
		if sql[-4:] == " OR ":
			sql = sql[:-4]
		return sql
			
	@staticmethod
	def revertdegree(degree):
		return str(degree* 600000)
	@staticmethod
	#lon is string
	def lngdiff(lon1,lon2):
		return '( '+lon1+' - '+lon2+')'
	
	@staticmethod
	#lon is string
	def latdiff(lat1,lat2):
		return '( '+lat1+' - '+lat2+')'
	@staticmethod
	#centerlon centerlat is string, in rad
	def makeupdistance(centerlon,centerlat):
#		 return '(2 * ASIN(SQRT(SIN( '+mysqlQuery.latdiff(centerlat,mysqlQuery.latcolrad)+' /2)*SIN( '+mysqlQuery.latdiff(centerlat,mysqlQuery.latcolrad)\
#				+' /2)+ COS('+centerlat+' )*COS(' +mysqlQuery.latcolrad+')*SIN('\
#				+mysqlQuery.lngdiff(centerlon,mysqlQuery.loncolrad)+'/2)'\
#				+'*SIN('+mysqlQuery.lngdiff(centerlon,mysqlQuery.loncolrad)+'/2)))* 6371.0)'
		a  = '(SIN( '+mysqlQuery.latdiff(centerlat,mysqlQuery.latcolrad)+' /2)*SIN( '+mysqlQuery.latdiff(centerlat,mysqlQuery.latcolrad)+' /2)+ COS('\
	+centerlat+' )*COS(' +mysqlQuery.latcolrad+')*SIN('+mysqlQuery.lngdiff(centerlon,mysqlQuery.loncolrad)+'/2)*SIN('+mysqlQuery.lngdiff(centerlon,mysqlQuery.loncolrad)+'/2))'
		return '(2 * ATAN2(SQRT('+a+'),SQRT(1-'+a+'))*6371.0)'

	@staticmethod
	def makeupoutput(filetype,filename):

		print 'filetype:'+filetype
		print 'filename:' +filename
		if filetype == 'csv':
			return " into outfile '"+MYSQL_INFO['output_path']+filename+".csv' fields terminated by ',' lines terminated by '\r\n'"
	def run(self):
	   print 'start'
	   result = self.query()
	   
	   print result
	   self.callback()
	def callback(self):
	   self.queryconn.disconnect()


#ars ={
#	 'timestart': '1992',
#	 'timeend': '2015',
#	 'type' : 1,
#	 'pt1': '(1,2)',
#	 'pt2':'(3,4)',
#	 'mmsi':'20150813'
#	 }


	
#mysqldb = mysqlQuery()
#mysqldb.makeupsql(ars)

#print '(51.4778, -0.0015) lowerright point is '+str(getdespoint(-0.0015,51.4778,300.7,7.794))
#getlowerrightpoint(180,30,90,90)
