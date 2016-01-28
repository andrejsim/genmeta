# skos dictionary get
import urlparse
import urllib2
from xml.etree import ElementTree as ET
import xml.dom.minidom

url = "http://vocab.nerc.ac.uk/collection/P07/current/"

# <gmd:keyword>
# <sdn:SDN_ParameterDiscoveryCode codeSpace="SeaDataNet" codeListValue="ATVS" 
# codeList="http://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_ParameterDiscoveryCode">Atmospheric visibility and transparency</sdn:SDN_ParameterDiscoveryCode>
# </gmd:keyword>

# http://vocab.nerc.ac.uk/collection/P07/current/#air_temperature

#class Vocab(self):
req = urllib2.urlopen(url)
catXml = req.read()

vocab = []
# print xml...
#print catXml

# xml formater in lxml
tree = ET.fromstring(catXml)

#xmlf = xml.dom.minidom.parseString(catXml)
#pretty_xml_as_string = xmlf.toprettyxml()
#print pretty_xml_as_string

for v in tree.getiterator():
	if "prefLabel" in v.tag:
		#print v.text
		vocab.append(v.text)

print vocab

# <gco:CharacterString>Climate and Forecast Standard Names</gco:CharacterString>

def check(term):

	if term in vocab:
		return True
	else:
		return False


print check("change_over_time_in_air_temperature")
print check("air_temperature")