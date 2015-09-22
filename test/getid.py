import time

day = ''
dayindex = 0

def gettaskid():
	global day
	global dayindex
	if day == '':
		day = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
		dayindex += 1
		return '{0}-{1}'.format(day,dayindex)
	
	lastday = time.strptime(day,"%Y-%m-%d-%H-%M-%S").tm_mday
	if time.localtime().tm_mday != lastday:
		day = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
		dayindex = 1
	else:
		dayindex += 1

	return '{0}-{1}'.format(day,dayindex)


if __name__ == '__main__':
	print gettaskid()
	print gettaskid()
	print gettaskid()
	print gettaskid()
	print gettaskid()