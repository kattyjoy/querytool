import os, zipfile, time
number = 1
last_file_start = None

class filetozip:  
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    #压缩文件
    def tozip(self):
        filelist = []
        if os.path.isfile(self.src):
            filelist.append(self.src)
        else:
            for root, dirs, files in os.walk(self.src):
                for name in files:
                    filelist.append(os.path.join(root, name))
        zipfilename = self.filename()
        print zipfilename
        zf = zipfile.ZipFile(zipfilename, 'w', zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname = tar[len(self.src):]
            zf.write(tar, arcname)
        zf.close()
        global number
        number += 1
    #zip文件名
    def filename(self):
        filename_start = time.strftime('%Y%m%d_',time.localtime(time.time()))
        global last_file_start
        global number
        if last_file_start == filename_start:
            filename_end = str(number)
        else:
            number = 1
            filename_end = str(number)
        last_file_start = filename_start

        return self.dst + filename_start + filename_end + '.zip'
'''
a = filetozip('F:\\b','F:\\')
a.tozip()
'''
