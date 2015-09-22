
import MySQLdb as mysql

import json

def tasklist():
	'''
	query and return task summary log for web
	'''

	#db = mysql.connect(MYSQL_INFO['host'], MYSQL_INFO['user'], MYSQL_INFO['passwd'], MYSQL_INFO['db'])
	db = mysql.connect('10.5.0.189', 'wsn', 'sensor', 'ais_dby')
	cursor = db.cursor()

	cursor.execute('SELECT count(*) from tasklog;')
	count = cursor.fetchall()[0][0]

	startindex = 10
	endindex = 20
	print count

	cursor.execute('SELECT id, taskid, starttime, status FROM tasklog ORDER BY id desc limit {0} offset {1};'.format(startindex, endindex-startindex))
	items = cursor.fetchall()

	print items
	#print data
	data = []

	for t in items:
		data.append({'id': t[0], 'taskid': t[1], 'starttime': str(t[2]) ,'status': t[3]})

	print data

	print json.dumps(data)

if __name__ == '__main__':
	tasklist()

'''
	for i in range(count / 10):
		cursor.execute('SELECT id, taskid, starttime, status FROM tasklog ORDER BY id desc limit {0} offset {1};'.format(10, i*10))
		print list(cursor.fetchall())
		print 'Page:{0}'.format(i+1)
		print ''
		print ''
'''