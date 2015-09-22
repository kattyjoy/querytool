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
		cursor.execute('SELECT id, taskid, starttime, status FROM tasklog ORDER BY id DESC limit {0} offset {1};'.format(startindex, endindex-startindex))
		items = cursor.fetchall()

		data = json.dump(items)
		print data
		print 'page: {0}'.format(page)
		db.commit()
		db.close()

		return render_template("tasktable.html", data)

	return render_template("tasklist.html")