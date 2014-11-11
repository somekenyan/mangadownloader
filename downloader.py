import os
import urllib
import threading
#import workerpool

class DownloadJob(threading.Thread):
	def __init__(self, link, name):
		threading.Thread.__init__(self)
		self.link = link
		self.name = name

	def run(self):
		urllib.urlretrieve(self.link, self.name)	

def downloadMangaImages(directory, diction):
	threads =[]
	for name in diction:
		s=directory+ name +'.'+ diction[name].split('.')[-1]
		t = DownloadJob(diction[name], s)
		threads.append(t)	

	for i in range(0, len(threads)):
		threads[i].start()

	for i in range(0, len(threads)):
		threads[i].join()


#def downloadMangaImages(diction):
#	pool = workerpool.WorkerPool(size=5)
#	for name in diction:
#		job = DownloadJob(name, diction[name])
#		pool.put(job)
#	pool.shutdown()
#	pool.wait()
#using the above class
#list{}
#pool = workerpool.WorkerPool(size=5)
#for url in list:
#	job = DownloadJob(url.strip())
#	pool.put(job)

#pool.shutdown()
#pool.wait()

