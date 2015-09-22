# encoding: utf-8
__author__ = "diaoboyu"

from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext
import os
import time
from threading import Thread

from callnglat import getdespoint, getlowerrightpoint, revertdegree_f, callnglat
from config import HIVEFILEPATH, DATAFILEPATH


class sparkQuery(Thread):
	"""docstring for sparkQuer y"""
	def __init__(self, timestart=0, timeend=0, tp=0, pt1=(0,0), pt2=(0,0), mmsi=['0'], output='csv', taskid=''):
		super(sparkQuery, self).__init__()
		self.sc = SparkContext(appName="ais_query" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) ,\
							   pyFiles=['./callnglat.py'])
		self.timestart 	= timestart
		self.timeend 	= timeend
		self.tp 		= tp
		self.pt1 		= pt1
		self.pt2 		= pt2
		self.mmsi		= mmsi
		self.output		= output
		self.rangeList 	= []
		self.taskid 	= taskid

		self.seprateYear()

	def seprateYear(self):
		# get years
		print "in query"
		startyear = time.localtime(self.timestart).tm_year
		endyear = time.localtime(self.timeend).tm_year

		print startyear, endyear

		if startyear < 2012:
			return
		if endyear > 2015:
			return 
		tmpstart = startyear
		# diff year
		if tmpstart != endyear:
			endofstartyear = time.mktime(time.strptime(str(startyear)+'-12-31-23:59:59', "%Y-%m-%d-%H:%M:%S"))
			#self.queryHive(timestart, endofstartyear, self.tp, self.pt1, self.pt2, self.mmsi, self.output)
			self.rangeList.append((self.timestart, endofstartyear))
			tmpstart += 1

		while tmpstart != endyear:
			startofthisyear = time.mktime(time.strptime(str(tmpstart)+'-01-01-00:00:00', "%Y-%m-%d-%H:%M:%S"))
			endofthisyear = time.mktime(time.strptime(str(tmpstart)+'-12-31-23:59:59', "%Y-%m-%d-%H:%M:%S"))
			#self.queryHive(startofthisyear, endofthisyear, self.tp, self.pt1, self.pt2, self.mmsi, self.output)	
			self.rangeList.append((startofthisyear, endofthisyear))
			tmpstart += 1

		startofendyear = time.mktime(time.strptime(str(endyear)+'-01-01-00:00:00', "%Y-%m-%d-%H:%M:%S"))
		#self.queryHive(startofendyear, timeend, self.tp, self.pt1, self.pt2, self.mmsi, self.output)
		self.rangeList.append((startofendyear, self.timeend))
	
	def callback(self):
		self.sc.stop()
		print "In callBack"
		pass

	def run(self):
		#try:
		for r in self.rangeList:
			tablename = self.queryHive(r[0], r[1], self.tp, self.pt1, self.pt2, self.mmsi, self.output, self.taskid)
			#merge file from hive tables here
			datafilepath = DATAFILEPATH.format(self.taskid)
			tablefilepath = HIVEFILEPATH.format(tablename)

			#ex: DATAFILEPATH/taskid/
			cmd_mkdir = "mkdir {0}".format(datafilepath)
			#ex:
			cmd_mergefile = "hadoop fs -cat {0} > {1}/{2}.csv".format(tablefilepath, datafilepath, self.taskid)

			print "cmd_mkdir {0}".format(cmd_mkdir)
			print "cmd_mergefile {0}".format(cmd_mergefile)

			os.system(cmd_mkdir)
			os.system(cmd_mergefile)

		self.callback()	

	def queryHive(self, timestart=0, timeend=0, tp=1, pt1= (0,0), pt2=(0,0), mmsi=['0'], output='csv', taskid=''):
		'''

		:param timestart:
		:param timeend:
		:param tp:
		:param pt1:
		:param pt2:
		:param mmsi:
		:param output:
		:param taskid:

		:return:
			hivetableName
		'''
		print "in queryHive"		
		year = time.localtime(timestart).tm_year
		sqlContext = HiveContext(self.sc)
		# time filter
		table = None
		print 'mmsi',mmsi
		if mmsi[0] != '0':
			#for x mmsi:
			table = sqlContext.sql("select * from aisdynamiclog_{0} where drterminalcode={1}".format(year, mmsi[0])).rdd
		else:
			table = sqlContext.sql("select * from aisdynamiclog_{0}".format(year)).rdd
		#table.cache()
		#print table.count()
		# space filter
		rltrdd = None

		if tp == 0:
			pt2 = getlowerrightpoint(pt1[0], pt1[1], pt2[0], pt2[1])
			pt_times1 = (revertdegree_f(pt1[0]), revertdegree_f(pt1[1]))
			pt_times2 = (revertdegree_f(pt2[0]), revertdegree_f(pt2[1]))
		if tp == 1:
			pt_times1 = (revertdegree_f(pt1[0]), revertdegree_f(pt1[1]))
			pt_times2 = (revertdegree_f(pt2[0]), revertdegree_f(pt2[1]))
		if tp == 2:
			pt_times1 = (revertdegree_f(pt1[0]), revertdegree_f(pt1[1]))

		if tp == 0 or tp == 1:
			rltrdd = table.filter(lambda row: callnglat.inside0_1(row, pt_times1, pt_times2))
		elif tp == 2:
			rltrdd = table.filter(lambda row: callnglat.inside2(row, pt_times1, pt2[0]))

		#empty rdd
		if rltrdd.count() == 0:
			return
		newdf = sqlContext.createDataFrame(rltrdd)

		# regist with a unique name
		tablename = "tmptable"
		newdf.registerAsTable(tablename)

		#hivetablename = "testtable3"
		hivetablename = "query_{0}_{1}".format(taskid, year)

		sql_create = "CREATE TABLE IF NOT EXISTS {0} \
				ROW FORMAT DELIMITED FIELDS TERMINATED BY \',\' LINES TERMINATED BY \'\\n\' \
				AS SELECT * from ais_model where 1=0".format(hivetablename)

		sql_insert = "INSERT INTO TABLE {0} select * from {1}".format(hivetablename, tablename)

		sqlContext.sql(sql_create)
		sqlContext.sql(sql_insert)

		return hivetablename





if __name__ == '__main__':
	sc = sparkQuery(timestart=1335801600, timeend=1430490142)
	#sc.query()
	sc.start()


