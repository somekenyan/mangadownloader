import urllib
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
#constant variables
	CONST_IMAGE = 1
	CONST_CHAPTER =2

	found = False
	type = 0

	image =1
	def __init__(self):
		HTMLParser.__init__(self)
		self.found = False

	def handle_starttag(self, tag, attrs):
		if self.type == self.CONST_IMAGE:
			self.getImageLink(tag, attrs)
		elif self.type == self.CONST_CHAPTER:
			self.getChapters(tag, attrs)
	def handle_endtag(self, tag):
		if self.found == True:
			if tag == "div":
				self.found = False
#	def handle_data(self, data):

	def downloadSth(self, data, t):
		self.type =t
		self.feed(data)

#		print "data ", data
	def getImageLink(self, tag, attrs):
		if tag == "div":
			for name, value in attrs:
				if name == 'id' and value == 'imgholder':
					self.found = True
		if self.found == True:
			if tag == "img":
				for name, value in attrs:
					if name == 'src':
						print value

#	def stopImageLink():
	def getChapters(self, tag, attrs):
		if tag == 'div':
			for name, value in attrs:
				if name == 'id' and value =='selectpage':
					self.found = True
		if self.found == True and tag == 'option':
			for name, value in attrs:
				if name == 'value':
					print value 

def downloadImage(link, name):
	urllib.urlretrieve(link, name)

def getPageImage(link):
	print link
	sock = urllib.urlopen(link)
	htmlSource = sock.read()
	sock.close()
	parser = MyHTMLParser()
	parser.downloadSth(htmlSource,2 )


