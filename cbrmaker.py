import os
import zipfile
import shutil


def makeCBR(directory):
	s = directory
	if s.endswith('/'):
		s = s[:-len('/')]
	comicname = s+'.cbz'
	zf = zipfile.ZipFile(comicname, "w",zipfile.ZIP_DEFLATED)
	for dirname, subdirs, files in os.walk(directory):
		zf.write(dirname)
		for filename in files:
			zf.write(os.path.join(dirname, filename))
	zf.close()
	#shutil.rmtree(directory)
	

#makeCBR("one.cbr","onepiece")
#directory = "onepiece"
#zf = zipfile.ZipFile("myzipfile.cbr", "w")
#for dirname, subdirs, files in os.walk(directory):
#	zf.write(dirname)
#	for filename in files:
#		zf.write(os.path.join(dirname, filename))
#zf.close
