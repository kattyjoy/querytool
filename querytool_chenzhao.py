# encoding: utf-8
__author__ = "diaoboyu"

import os
#from flaskext.mysql import MySQL
from flask import Flask,request,g,redirect,url_for,render_template,flash,session
from functools import wraps

from config import MYSQL_INFO

#from sparkquery import sparkQuery
from mysqlquery import mysqlQuery
import MySQLdb as mysql
import threading

import json

# init flask app
app = Flask(__name__)
app.config.from_object(__name__)

app.config['MYSQL_DATABASE_HOST'] = MYSQL_INFO['host']
app.config['MYSQL_DATABASE_DB'] = MYSQL_INFO['db']
app.config['MYSQL_DATABASE_USER'] = MYSQL_INFO['user']
app.config['MYSQL_DATABASE_PASSWORD'] = MYSQL_INFO['passwd']


def general_query(source='hive', timestart=0, timeend=0, tp=0, pt1=(0,0), pt2=(0,0), mmsi=[0], output='csv'):
	'''general query function
		Args:
			source: 	data source, include 'hive', 'mysql', 'oracle'
			timestart:	start time of query range
			timeend:	end time of query range
			type:		space query type, 
						0: pt1 is upper left (lo,la) coordinate, pt2 is (vertical, horizontal) length
						1: pt1 is upper left (lo,la) coordinate, pt2 is lower right (lo,la) coordinate
						2: pt1 is the centor of the circle and pt2 is (R,0) where R is the redius
			pt1:		(lo,la) point
			pt2:		see 'type'
			mmsi:		-1: all mmsi
						list:	a single or list of mmsi
			output		output file format, include 'csv', 'xls', 'txt', etc.
		Returns：

	'''
	pass
#	if source == 'hive':
#		print 'source is hive'
#		sq = sparkQuery(timestart, timeend, tp, pt1, pt2, mmsi, output)
#		sq.start()
		#sq.querytest(mmsi)
#	elif source == 'mysql':
#		print 'source is mysql'
 #               mq = mysqlQuery(timestart, timeend, tp, pt1, pt2, mmsi, output)
	#	mq.start()
		
#	elif source == 'oracle':
#		pass
@app.route('/validquery', methods=['POST'])
def valiequery():
	if request.method == 'POST':
		print request.form

#		general_query(source	=	request.form['datasourceSelect'], \
#					  timestart =	float(request.form['starttime']), \
#					  timeend	=	float(request.form['endtime']), \
#					  tp 		=	int(request.form['tp']), \
#					  pt1		=	tuple([float(x) for x in request.form['pt1'].split(',')]), \
#					  pt2		=	tuple([float(x) for x in request.form['pt2'].split(',')]), \
#					  mmsi		=	request.form['MMSIship'].split(','), \
#					  output	=	request.form['filetype']
#					  )
		data = {'waittime':u"30分钟"}
		print json.dumps(data)
		return json.dumps(data)

@app.route('/tasklist', methods=['GET','POST'])
def tasklist():
	if request.method == 'POST':
		'''
		query and return task summary log for web
		'''
		#print request.args
		#page = int(request.form['pageindex'])
		startindex = int(request.form['startindex'])
		endindex = int(request.form['endindex'])

		if startindex >= endindex:
			return

		db = mysql.connect(MYSQL_INFO['host'], MYSQL_INFO['user'], MYSQL_INFO['passwd'], MYSQL_INFO['db'])
		cursor = db.cursor()

		cursor.execute('SELECT count(*) from tasklog;')
		count = cursor.fetchall()[0][0]

		print count

		#for i in range(count / MYSQL_INFO['page_size'] + 1):
		cursor.execute('SELECT id, taskid, starttime, status FROM tasklog ORDER BY id DESC limit {1} offset {0};'.format(startindex, endindex-startindex))
		items = cursor.fetchall()
		data = []
		for t in items:
			data.append({'id': t[0], 'taskid': t[1], 'starttime': str(t[2]) ,'status': t[3]})
		print json.dumps(data)
		print 'records : {0} to {1}'.format(startindex+1,endindex)
		db.commit()
		db.close()

		return json.dumps(data)
	return render_template("tasklist.html")
@app.route('/tasktotal',methods=['POST'])
def tasktotal():
		db = mysql.connect(MYSQL_INFO['host'], MYSQL_INFO['user'], MYSQL_INFO['passwd'], MYSQL_INFO['db'])
		cursor = db.cursor()

		cursor.execute('SELECT count(*) from tasklog;')
		count = cursor.fetchall()[0][0]

		print 'total'+str(count)
		return str(count)
@app.route('/taskdetail', methods=['GET'])
def taskdetail():
	'''
	query and return task detail log for web
	'''

	db = mysql.connect(MYSQL_INFO['host'], MYSQL_INFO['user'], MYSQL_INFO['passwd'], MYSQL_INFO['db'])
	cursor = db.cursor()

	#cursor.execute('SELECT * from tasklog where taskid == ;')
	#count = cursor.fetchall()

	#pass
	

@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
	if request.method == 'POST':
		print request.form
		return "recieve:[[[ "+str(request.form)+"]]]"
	return render_template('home.html') 
#		general_query(source	=	request.form['datasourceSelect'], \
#					  timestart =	float(request.form['starttime']), \
#					  timeend	=	float(request.form['endtime']), \
#					  tp 		=	int(request.form['tp']), \
#					  pt1		=	tuple([float(x) for x in request.form['pt1'].split(',')]), \
#					  pt2		=	tuple([float(x) for x in request.form['pt2'].split(',')]), \
#					  mmsi		=	request.form['MMSIship'].split(','), \
#					  output	=	request.form['filetype']
#					  )
#	return render_template('home.html')

if __name__=='__main__':
	app.run(host="127.0.0.1", port=5000, debug=True)
