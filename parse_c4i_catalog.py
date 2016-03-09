import urlparse
import urllib2
from xml.etree import ElementTree as ET

#wmsStart = 'https://climate4impact.eu/impactportal/ImpactService?source='
#catalog = 'http://opendap.knmi.nl/knmi/thredds/catalog/'
#opendap = 'http://opendap.knmi.nl/knmi/thredds/dodsC/'
#wmsEnd = '&service=WMS&'

def readThreddsCatalog(url,project,data):

	link = url+'catalog/'+project+'/catalog.xml'
	
	#print "read thredds: "+ link

	req = urllib2.urlopen(link)

	catXml = req.read()

	tree = ET.fromstring(catXml)

	listLinks = tree.getiterator()

	for u in listLinks:
		if 'catalogRef' in u.tag:
			nextlink = u.get('ID')+'/catalog.xml'
			if nextlink is not None:
				#data.append( link.replace('catalog.xml',nextlink ) )
				readThreddsCatalog( url , u.get('ID') , data)
		elif 'dataset' in u.tag:
			nclink = u.get('urlPath')
			if nclink is not None:
				#print nclink
				if 'zip' not in nclink:
					key = project.replace('/','_').replace('-','_')		
					if key not in data.keys():
						data[key] = [] # new list...
					data[key].append( url +'dodsC/'+nclink )
				
			
#top level parse
def readcatalog(url):
	req = urllib2.urlopen(url)
	catXml = req.read()

	# printxml...
	#print catXml

	# xml formater in lxml
	tree = ET.fromstring(catXml)
	#
	#ns = { "" : "http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0" }

	#print '{'+tree.get('xmlns')+'}'
	#print tree.find('{http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0}catalog',ns)

	listLinks = tree.getiterator()
	#print "\nlinks"
	#xpath //a all elements with a ... thus all links in html
	for u in listLinks:
		#print u.tag
		for k in u.keys():
			if "ID" in k:
				link = u.get(k)

				newlink = catalog + link + "/catalog.xml"

				#print newlink
				readcatalog2(newlink)


def readcatalogB(catalog, url):
	req = urllib2.urlopen(catalog+url)
	catXml = req.read()

	# xml formater in lxml
	tree = ET.fromstring(catXml)
	#

	listLinks = tree.getiterator()
	#print "\nlinks"
	layers    = []
	newLinks = []
	#xpath //a all elements with a ... thus all links in html

	for u in listLinks:
		for k in u.keys():
			if "title" in k:
				layers.append(u.get(k,'{http://www.w3.org/1999/xlink}'))
			if "ID" in k:
				link = u.get(k)

				newlink = catalog + link + "/catalog.xml"

				#print newlink
				newLinks.append(newlink)	
	return (layers , newLinks)


from collections import OrderedDict

def readcatalogC(catalog, url,base):
	req = urllib2.urlopen(catalog+url)
	catXml = req.read()

	# xml formater in lxml
	tree = ET.fromstring(catXml)
	#
	listLinks = tree.getiterator()

	#print "\nlinks"
	layers    = []
	links = []
	#xpath //a all elements with a ... thus all links in html
	dict = OrderedDict()
	for u in listLinks:
		for k in u.keys():
			if "urlPath" in k:
				l = u.get(k).split('/')[3]
				layers.append(l)
			if "ID" in k:
				link = u.get(k)
				newlink = base + link #+ "/catalog.xml"

				#print newlink
				links.append(newlink)	
				
	for i in len(layers): 			
		dicto[layers[i]].append(links)

	return dicto 

#mid level parse
def readcatalog2B(catalog,url):
	req = urllib2.urlopen(url)
	catXml = req.read()

	# printxml...
	#print catXml

	# xml formater in lxml
	tree = ET.fromstring(catXml)
	#
	listLinks = tree.getiterator()
	#xpath //a all elements with a ... thus all links in html
	newLinks = []
	for u in listLinks:
		#print u.tag, ' ', u
		if "catalogRef" in u.tag:
			link = u.get("ID")

			newlink = catalog + link + "/catalog.xml"
			newLinks.append(newlink)

	return newLinks

def readcatalog2C(catalog0,url):
	req = urllib2.urlopen(url)
	catXml = req.read()

	# printxml...
	print catXml

	# xml formater in lxml
	tree = ET.fromstring(catXml)
	#
	listLinks = tree.getiterator()
	#xpath //a all elements with a ... thus all links in html
	newLinks = []
	for u in listLinks:
		#print u.tag, ' ', u
		if "dataset" in u.tag:
			link = u.get("name")

			newlink = catalog0 + link #+ "/catalog.xml"
			newLinks.append(newlink)

	return newLinks


#mid level parse
def readcatalog2(url):
	newlink =  readcatalog2B(url)
	#print newlink
	readcatalog3( newlink )

#bottom level parse
def readcatalog3(url,opendap,wmsStart,wmsEnd):
	req = urllib2.urlopen(url)
	catXml = req.read()

	wmsAnswer = []
	ncAnswer  = []

	# xml formater in lxml
	tree = ET.fromstring(catXml)

	#
	listLinks = tree.getiterator()

	#xpath //a all elements with a ... thus all links in html
	for u in listLinks:
		if "dataset" in u.tag:
			ilink = u.get("ID")
			if ".nc" in ilink:
				wmsAnswer.append( wmsStart+opendap+ilink+wmsEnd )	
				ncAnswer.append( opendap+ilink )	

	return (wmsAnswer , ncAnswer)	

#bottom level parse
def readcatalog3B(url,opendap,wmsStart,wmsEnd,layer):
	req = urllib2.urlopen(url)
	catXml = req.read()

	# xml formater in lxml
	tree = ET.fromstring(catXml)

	#
	listLinks = tree.getiterator()
	#print "\nlinks"
	#xpath //a all elements with a ... thus all links in html
	for u in listLinks:
		#for k in u.keys():
		if "dataset" in u.tag:
			ilink = u.get("urlPath")
			idlink = u.get("ID")
			if ilink is None:
				print ''
			elif ".nc" in ilink:
				if layer in ilink:
					#print url
					wmsAnswer.append( wmsStart+ilink+wmsEnd )	
					ncAnswer.append( opendap+ilink )	
					
	return (wmsAnswer , ncAnswer)	
					
# req link
#firsturl = 'http://opendap.knmi.nl/knmi/thredds/catalog/CLIPC/tier1_indicators/icclim_cerfacs/vDTR/MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1/catalog.xml'
#firsturl = 'http://opendap.knmi.nl/knmi/thredds/catalog/CLIPC/tier1_indicators/icclim_cerfacs/vDTR/EURO4M_MESANv1/catalog.xml'
#readcatalog3(firsturl)

#firsturl = 'http://opendap.knmi.nl/knmi/thredds/catalog/CLIPC/tier1_indicators/icclim_cerfacs/vDTR/catalog.xml'
#readcatalog2(firsturl)

#firsturl = 'http://opendap.knmi.nl/knmi/thredds/catalog/CLIPC/tier1_indicators/icclim_cerfacs/catalog.xml'
#readcatalog(firsturl)

wmsAnswer = []
ncAnswer  = []

def readcatalog4(url,opendap,wmsStart,wmsEnd):
	req = urllib2.urlopen(url)
	catXml = req.read()

	# xml formater in lxml
	tree = ET.fromstring(catXml)
	
	#
	listLinks = tree.getiterator()
	#print "\nlinks"
	#xpath //a all elements with a ... thus all links in html
	for u in listLinks:
		#for k in u.keys():
		if "dataset" in u.tag:
			ilink = u.get("urlPath")
			#print ilink
			if ilink is None:
				print ""
			elif ".nc" in ilink:
				wmsAnswer.append( wmsStart+opendap+ilink+wmsEnd )	
				ncAnswer.append( opendap+ilink )	
		elif "catalogRef" in u.tag:
			#print u.attrib
			rep =  u.get("{http://www.w3.org/1999/xlink}href")
			readcatalog4( url.replace('catalog.xml',rep) ,opendap,wmsStart,wmsEnd )

	return (wmsAnswer , ncAnswer)	
