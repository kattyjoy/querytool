import math

earthR = 6371.0

class callnglat(object):
        @staticmethod
        def inside2(row, point, r):

                '''
                        a center of circle and radius
		        '''

                pass
                return True
        @staticmethod
        def inside0_1(row, point1, point2):
                '''
	Args:
		point1 (x1, y1): leftup point in float
		point2 (x2, y2: rightdown point in float

		pt1.x > pt2.x indicate that the rectangle cover the 180 E line
		so we should separate the rectangle into two parts

		pt1.x to 180E, 180W to pt2.x

		pt1.x < pt2.x is normal
		x1 < lng < x2
		y1 < log < y2

		row
		row[5] lag * 600000
		row[6] lng * 600000

		180*600000 =
	Returns
		return Bool
	    '''
                if row[5] == None or row[6] == None:
                        return False

                if point1[0] <= point2[0]:
                        if (point1[0] <= float(row[6]) <= point2[0]) and (point2[1] <= float(row[5]) <= point1[1]):
                                return True
                else:
                        if (point1[0] <= float(row[6]) <= 108000000) and (-108000000 <= float(row[6]) <= point2[0]) and \
                                (point2[1] <= row[5] <= point1[1]):
                                return True
                return False

def getlowerrightpoint(lng,lat,vertical, horizontal):
        rightlongitude = getdespoint(lng,lat,90,horizontal)[0]
        rightlatitude = getdespoint(lng,lat,180,vertical)[1]
        print '('+str(lng)+'Lng,'+str(lat)+'Lat) lowerright point is ('+str(rightlongitude)+'Lng,'+str(rightlatitude)+'Lat) with vertical '+str(vertical)+'km,horizontal '+str(horizontal)+'km'
        return (rightlongitude,rightlatitude)


def getdespoint(lng1,lat1,ang,distance):
        #return destination (longitude,latitude)
        latitude1 =  math.radians(lat1)
        longitude1 =  math.radians(lng1)
        angle = math.radians(ang)
        angular = distance / earthR
        latitude2 = math.asin(math.sin(latitude1)*math.cos(angular)+math.cos(latitude1)*math.sin(angular)*math.cos(angle))
#        longitude2 = longitude1 + math.atan2(math.sin(angle)*math.sin(angular)*math.cos(latitude1),math.cos(angle)-math.sin(latitude1)*math.sin(latitude2))
        longitude2 = longitude1 + math.atan2(math.sin(angle)*math.sin(angular)*math.cos(latitude1),math.cos(angular)-math.sin(latitude1)*math.sin(latitude2))
        latitude2 = math.degrees(latitude2)
        if latitude2 < -90:
            latitude2 = -90
        longitude2 = (longitude2 +3*math.pi)%(2*math.pi) - math.pi
        longitude2 = math.degrees(longitude2)
        print 'point ('+str(lng1)+','+str(lat1)+') getdespoint: ('+str(longitude2)+','+str(latitude2)+')'+'with distance '+str(distance)+'km and angel: '+str(ang)
        return (longitude2,latitude2)

def revertdegree(degree):
        return str(degree * 600000)
def revertdegree_f(degree):
        return degree * 600000
    


