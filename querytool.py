# encoding: utf-8
__author__ = "diaoboyu"

import os
#from flaskext.mysql import MySQL
from flask import Flask,request,g,redirect,url_for,render_template,flash,session,make_response,jsonify
from functools import wraps

from config import MYSQL_INFO,MYSQL_DB_INFO,SEARCH_NAME_CONFIG

#from sparkquery import sparkQuery
from mysqlquery import mysqlQuery
from tasklog import TaskLog
import MySQLdb as mysql

import types
import threading
import json
import math
import time
#from werkzeug import secure_filename
# init flask app
app = Flask(__name__)
app.config.from_object(__name__)

#UPLOAD_FOLDER = '/uploadtmp'
#ALLOWD_EXTENSIONS = set(['txt','csv'])
app.config['MYSQL_DATABASE_HOST'] = MYSQL_INFO['host']
app.config['MYSQL_DATABASE_USER'] = MYSQL_INFO['user']
app.config['MYSQL_DATABASE_PASSWORD'] = MYSQL_INFO['passwd']
app.config['JSON_AS_ASCII'] = False
app.config['SEARCH_NAME_CONFIG'] = SEARCH_NAME_CONFIG
app.config['FORM'] = 'queryform'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
def degtodms(degree = 0.0,lngflag = False):
	value = math.fabs(degree)
	deg = int(math.floor(value))
	minute = int(math.floor((value - deg) * 60))
	second = int(math.floor(((value - deg) * 60 - minute) * 60))
	if degree >= 0:
		if lngflag :
			return u"东经 {0}°{1}′{2}″".format(deg,minute,second)
		else:
			return u"北纬 {0}°{1}′{2}″".format(deg,minute,second)
	else:
		if lngflag :
			return u"西经 {0}°{1}′{2}″".format(deg,minute,second)
		else:
			return u"南纬 {0}°{1}′{2}″".format(deg,minute,second)

def general_query(formdict={}):
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
#	taskid = TaskLog.insertlog(formdict['source'],'0', '1', 'type','pt1', 'pt2', str(formdict['mmsi']), formdict['output'])
	taskid = TaskLog.getnewtaskid()
	timelist = []
	for t in formdict['date']:
		timelist.append(tuple(t.split(',')))
	print "timelist:"
	print timelist
	
	
	positionlist = []
	for p in formdict['position']:
		if p['postype'] == "geo":
			itemdict = {'tp':p['tp'],'pt1':tuple([float(x) for x in p['pt1'].split(',')]),'pt2':tuple(tuple([float(x) for x in p['pt2'].split(',')]))}
			positionlist.append(itemdict)
		elif p['postype'] == "port":
			print 'name:'+p['name']
	print "positionlist:"
	print positionlist



	if formdict['source'] == 'hive':
		print 'source is hive'
#		sq = sparkQuery(timestart, timeend, tp, pt1, pt2, mmsi, output, taskid)
#		sq.start()
		#sq.querytest(mmsi)
	elif formdict['source'] == 'mysql':
		print 'source is mysql'
		mq = mysqlQuery(timelist,positionlist,mmsilist=formdict['mmsi'],countrylist = formdict['country'],output=formdict['output'],taskid =taskid)
		mq.start()
		
	elif source == 'oracle':
		pass


@app.route('/validquery', methods=['POST'])
def validquery():
	if request.method == 'POST':
		print "validquery"
		print 'request.form'
		print request.form
		print 'request.get_json()'
		print type(request.get_json())
		requestpython = request.get_json()
		for  key in requestpython.keys():
			print key+": "+str(requestpython[key])
		#general_query(source	=	request.form['datasourceSelect'], \
		#			  timestart =	float(request.form['starttime']), \
		#			  timeend	=	float(request.form['endtime']), \
	#				  tp 		=	int(request.form['tp']), \
	#				  pt1		=	tuple([float(x) for x in request.form['pt1'].split(',')]), \
	#				  pt2		=	tuple([float(x) for x in request.form['pt2'].split(',')]), \
	#				  mmsi		=	request.form['MMSIship'].split(','), \
	#				  output	=	request.form['filetype'] \
	#				  )
		general_query(request.get_json())
		print jsonify({'waittime':u"30分钟 "})
		return jsonify({'waittime':u"30分钟 "})
		#return make_response(json.dumps(data))
	return make_response(json.dumps({}))
		#return "recieve:[[[ "+str(request.form)+"]]]"


@app.route('/tasklist', methods=['GET', 'POST'])
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
			return make_response("{}")
		items = TaskLog.getlist(startindex,endindex)

		data = []
		for t in items:
			data.append({'id': t[0], 'taskid': t[1], 'starttime': str(t[2]) ,'status': t[3]})
		print json.dumps(data)
		print 'records : {0} to {1}'.format(startindex+1,endindex)

		return make_response(json.dumps(data))
	return render_template("tasklist.html")
	

@app.route('/taskdetail', methods=['POST'])
def taskdetail():
	'''
	query and return task detail log for web
	'''
	print request.form
	taskid = request.form['taskid']

	item = TaskLog.getdetail(taskid)
	print item
	if type(item) is types.StringType:
		return item
	typedict = [u'矩形(一点)',u'矩形(两点)',u'圆形']
	leftone = [u'左上经度',u'左上经度',u'圆心经度']
	rightone = [u'左上纬度',u'左上纬度',u'圆心纬度']
	lefttwo = [u'长度(km)',u'右下经度',u'半径(km)']
	righttwo = [u'宽度(km)',u'右下纬度','']
	data = {'taskid': item[1], 'source': item[2], 'timestart': item[3], 'timeend': item[4] \
		, 'tp': item[5], 'pt1': tuple([float(x) for x in  item[6][1:-1].split(',')]) \
		, 'pt2': tuple([float(x) for x in  item[7][1:-1].split(',')]) , 'mmsi': item[8], 'opformat': item[9]}
	pt1 = ("","")
	pt2 = ("","")
	if data["tp"] == 0:
		pt1 = (degtodms(data["pt1"][0],True),degtodms(data["pt1"][1],False))
		pt2 = (str(data["pt2"][0]),str(data["pt2"][1]))
	elif data["tp"] == 1:
		pt1 = (degtodms(data["pt1"][0],True),degtodms(data["pt1"][1],False))
		pt2 = (degtodms(data["pt2"][0],True),degtodms(data["pt2"][1],False))
	elif data["tp"] == 2:
		pt1 = (degtodms(data["pt1"][0],True),degtodms(data["pt1"][1],False))
		pt2 = (str(data["pt2"][0]),"")

	lefts = [{'title':u'任务ID','value':data["taskid"]}, \
			{'title':u'开始时间','value':str(data["timestart"])}, \
			{'title':u'查询区域','value':typedict[data["tp"]]}, \
			{'title':leftone[data["tp"]],'value':pt1[0]}, \
			{'title':lefttwo[data["tp"]],'value':pt2[0]}]
	rights = [{'title':u'数据源','value':data["source"]}, \
			{'title':u'结束时间','value':str(data["timeend"])}, \
			{'title':u'导出格式','value':data["opformat"]}, \
			{'title':rightone[data["tp"]],'value':pt1[1]}, \
			{'title':righttwo[data["tp"]],'value':pt2[1]}]
	print "++||left||++"
	print str(lefts)
	print "++||right||++"
	print str(rights)
	if data["mmsi"] == "ALL":
		data["mmsi"] = u"全部"
	return render_template("taskdetail.html",lefts = lefts,rights = rights,mmsi = data["mmsi"])
	
@app.route('/tasktotal',methods=['POST'])
def tasktotal():
		count = TaskLog.gettaskcount()
		print 'total'+str(count)
		return make_response(str(count))

@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
	
	return render_template('home.html')
if __name__=='__main__':
	app.run( port=5000, debug=True)

	#app.run(host='10.5.0.237', port=5001, debug=True)
	#tasklist()

'''
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print file
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return ''

'''
    

