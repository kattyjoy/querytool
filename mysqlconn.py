# encoding: utf-8
__author__ = "chenzhao"
import os
import MySQLdb
import time
import traceback
import math
from config import MYSQL_INFO

class MySQLConn:
	def __init__(self,dbname):
		self.db = dbname
		self.tryconnect()
	def tryconnect(self):
		print 'try connect'
		try :
			self.conn = MySQLdb.connect(host=MYSQL_INFO['host'], \
										port=MYSQL_INFO['port'], \
										user=MYSQL_INFO['user'], \
										passwd=MYSQL_INFO['passwd'], \
										db=self.db)
		except MySQLdb.InterfaceError,e:
			print 'InterfaceError'
			print e.message
			print traceback.format_exc()
			self.tryconnect()
		except Exception,e:
			print 'OtherError'
			print e.message
			print traceback.format_exc()
		finally :
			try:
				self.conn.ping()
			except MySQLdb.InterfaceError,e:
				print 'InterfaceError'
				print e.message
				print traceback.format_exc()
				self.tryconnect()
			except Exception,e:
				print 'OtherError'
				print e.message
				print traceback.format_exc()
		print 'connect success'
	def disconnect(self):
		print 'disconnect....'
		try:
			self.conn.close()
		except Exception,e:
			print 'OtherError'
			print e.message
			print traceback.format_exc()
	def keepconn(self):
		try:
			self.conn.ping()
		except MySQLdb.InterfaceError,e:
		   #conn invalid 
			print e.message
			print traceback.format_exc()
			self.tryconnect()
		except MySQLdb.ProgrammingError,e:
			#cur invalid
			print e.message	
			print traceback.format_exc()
	def commit(self):
		self.conn.commit()
	def cursor(self):
		return self.conn.cursor()