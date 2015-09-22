# encoding: utf-8
import os
# infile = open("country.csv","r")
# outfile = open("tmp.txt","w")
# writelines = []
# for line in infile:
# 	print line
# 	c = line.split(',')
# 	print c
# 	c[1]= c[1][:-1]
# 	writelines.append('<option  data-subtext="'+c[0]+'" value="'+c[1]+'">'+c[1]+'</option>\n')
# print writelines
# outfile.writelines(writelines)
# infile.close()
# outfile.close()	

inzh = open("zh.txt","r")
ineng = open("eng.txt","r")
outfile = open("tmp.txt","w")
writelines = []
for line in ineng:
	line = line[:-1]
	print line
	zh = inzh.readline()
	zh = zh[:-1]
	print zh
	writelines.append('<option data-subtext="'+zh+'" value="'+line+'">'+line+'</option>\n')
print writelines
outfile.writelines(writelines)
inzh.close()
ineng.close()
outfile.close()