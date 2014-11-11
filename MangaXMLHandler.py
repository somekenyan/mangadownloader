from xml.dom.minidom import parse, Node
import xml.etree.ElementTree as etree

folder = "properties/"
xmlfile = 'sitesdata.xml'
propertiesfile = "properties.xml"

SITE= 'site'
SITE_LINK = 'link'
SITE_MANGALIST = 'mangalist'
SITE_NAME = 'name'
SITE_IMAGE = 'chapter_image'
SITE_CHAPTER = 'chapter_names'
SITE_MANGA = 'manga'
SITE_TITLE ='title'

SITE_TAG = 'tag'
SITE_TAG_ATTR= 'attr'
SITE_TAG_ATTR_VALUE = 'attr_value'
SITE_IMG_TAG = 'src'
SITE_SUBCONTAINER ='subcontainer'

def loadDocument(filename):
	tree = etree.parse(filename)
	return tree.getroot()

def getSite(siteName):
	root = loadDocument(folder+xmlfile)
	for site in root.findall(SITE):
		if site.find(SITE_NAME).text == siteName:
			return site
def getChapterImageTags(siteName):
	site = getSite(siteName)
	var = {}
	for chap in site.find(SITE_IMAGE):
		vs = site.find(SITE_IMAGE).find(SITE_SUBCONTAINER)
		if chap.tag ==SITE_TAG:
			var['root'] = chap.text
		elif chap.tag == SITE_TAG_ATTR:
			var['root_attr'] = chap.text
		elif chap.tag == SITE_TAG_ATTR_VALUE:
			var['root_attr_value'] = chap.text
		elif chap.tag == SITE_SUBCONTAINER:
			var['sub'] = {}
			for sub in vs:
				if sub.tag == SITE_TAG:
					var['sub']['root']= sub.text
				elif sub.tag == SITE_TAG_ATTR:
					var['sub']['root_attr'] = sub.text
				elif sub.tag == SITE_TAG_ATTR_VALUE:
					var['sub']['root_attr_value'] = sub.text
	return var

def getContainerTags(siteName, container):
	site = getSite(siteName)
	var={}
	for chap in site.find(container):
		vs = site.find(container).find(SITE_SUBCONTAINER)
		if chap.tag ==SITE_TAG:
			var['root'] = chap.text
		elif chap.tag == SITE_TAG_ATTR:
			var['root_attr'] = chap.text
		elif chap.tag == SITE_TAG_ATTR_VALUE:
			var['root_attr_value'] = chap.text
		elif chap.tag == SITE_SUBCONTAINER:
			var['sub'] = {}
			for sub in vs:
				print sub.tag
				if sub.tag == SITE_TAG:
					var['sub']['root']= sub.text
				elif sub.tag == SITE_TAG_ATTR:
					var['sub']['root_attr'] = sub.text
				elif sub.tag == SITE_TAG_ATTR_VALUE:
					var['sub']['root_attr_value'] = sub.text
	return var


def getChapterTags(siteName):
	return getContainerTags(siteName, SITE_CHAPTER)	
	

def getMangaTags(siteName):
	return getContainerTags(siteName, SITE_MANGA)

def getTitleTags(siteName):
	return getContainerTags(siteName, SITE_TITLE)

def getLink(siteName):
	site = getSite(siteName)
	return site.find(SITE_LINK).text

def getMangaList(siteName):
	site = getSite(siteName)
	return site.find(SITE_MANGALIST).text


#method for writing mangalist to a local file
def writeMangaList(siteName):
	print "not done"
#methods for writing xml

def writeSimpleXML():
	root = etree.Element('root')
	doc = etree.SubElement(root,'doc')
	field1 = etree.SubElement(doc,'field1')
	field1.set('name', 'blah')
	field1.text = 'somevalue1'
	
	field2= etree.SubElement(doc,'field2')
	field2.set('name', 'blah2')
	field2.text ='somevalue2'
	
	tree = etree.ElementTree(root)
	tree.write("filename.xml")

#writeSimpleXML()
#methods for getting and changing the download location
def getDownloadLocation():
	root = loadDocument(folder+propertiesfile)
	return root.find('location').text

def changeDownloadLocation(path):
	if path.endswith('/')== False:
		path = path +'/'
	root = loadDocument(folder+propertiesfile)
	loc = root.find('location')
	loc.text =path 
	tree = etree.ElementTree(root)
	tree.write(folder+propertiesfile)

#print getLink('mangapanda')
#chapter = getChapterTags('mangapanda')
#print chapter
#chapter = getChapterImageTags('onemanga')
#print chapter
#if chapter.has_key('ub'):
#	print 'working'
#site = getSite('mangapanda')
#print site.find('link').text
