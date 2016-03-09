import xml.etree.ElementTree as ET
import xml.dom.minidom
import skos_nerc_cf_vocab

#
# generate unique metadata document from template using etree.
#

def addKeyword(element, value,count):
	# skos cf vocab...
	if skos_nerc_cf_vocab.check(str(value)):
		#print value
		dk = ET.Element("{http://www.isotc211.org/2005/gmd}descriptiveKeywords")
		mk = ET.SubElement( dk,	"{http://www.isotc211.org/2005/gmd}MD_Keywords")
		kw = ET.SubElement( mk,	"{http://www.isotc211.org/2005/gmd}keyword")
		#sv = ET.SubElement( kw,	"{http://www.isotc211.org/2005/gco}CharacterString")
		
		sv = ET.SubElement( kw,	"{http://www.isotc211.org/2005/gmx}Anchor") #xmlns:gmx="http://www.isotc211.org/2005/gmx"
		sv.set("{http://www.w3.org/1999/xlink}label","skos")
		sv.set("{http://www.w3.org/1999/xlink}href",str("http://vocab.nerc.ac.uk/collection/P07/current/#"+value) )
		sv.set("{http://www.w3.org/1999/xlink}title",value)

		sv.text = value

		#tn = ET.SubElement( mk,	"{http://www.isotc211.org/2005/gmd}thesaurusName")
		#ct = ET.SubElement( tn,	"{http://www.isotc211.org/2005/gmd}CI_Citation")
		#tt = ET.SubElement( ct,	"{http://www.isotc211.org/2005/gmd}title")
		#cs = ET.SubElement( tt,	"{http://www.isotc211.org/2005/gco}CharacterString")
		#cs.text = "Climate and Forecast Standard Names"

	else: # standard keyword
		dk = ET.Element("{http://www.isotc211.org/2005/gmd}descriptiveKeywords")
		mk = ET.SubElement( dk,	"{http://www.isotc211.org/2005/gmd}MD_Keywords")
		kw = ET.SubElement( mk,	"{http://www.isotc211.org/2005/gmd}keyword")
		sv = ET.SubElement( kw,	"{http://www.isotc211.org/2005/gco}CharacterString")
		sv.text = value


	#index of last keyword element.
	element.insert(count,dk)

	#todo
	# if value in skos_dict:
	#	add element with dict...

def addOpendapResource(element, value):
	dk = ET.SubElement(element,"{http://www.isotc211.org/2005/gmd}onLine")
	mk = ET.SubElement( dk,	"{http://www.isotc211.org/2005/gmd}CI_OnlineResource")
	kw = ET.SubElement( mk,	"{http://www.isotc211.org/2005/gmd}linkage")
	sv = ET.SubElement( kw,	"{http://www.isotc211.org/2005/gmd}URL")
	sv.text = value
	nm = ET.SubElement( mk,	"{http://www.isotc211.org/2005/gmd}name")
	ch = ET.SubElement( nm,	"{http://www.isotc211.org/2005/gco}CharacterString")
	ch.text = 'OPeNDAP'
	nm = ET.SubElement( mk,	"{http://www.isotc211.org/2005/gmd}description")
	ch = ET.SubElement( nm,	"{http://www.isotc211.org/2005/gco}CharacterString")
	ch.text = 'THREDDS OPeNDAP'
	nm = ET.SubElement( mk,	"{http://www.isotc211.org/2005/gmd}function")
	ch = ET.SubElement( nm,	"{http://www.isotc211.org/2005/gmd}CI_OnLineFunctionCode")
	ch.set("codeList","http://www.ngdc.noaa.gov/metadata/published/xsd/schema/resources/Codelist/gmxCodelists.xml#CI_OnLineFunctionCode")
	ch.set("codeListValue","download")
	ch.text = 'download'

def replace_onlineResource( atree,
	ncurls, 
	wmslinks,  
	layer,
	keywords ):

	for element in atree.getroot().iter():
		#print element
		if "MD_DigitalTransferOptions" in element.tag: 
			
			for res in ncurls:		
				#opendap_link = res.replace('https://climate4impact.eu/impactportal/ImpactService?source=','').replace('&service=WMS&','')	
				opendap_link = res
				addOpendapResource(element,opendap_link)

			onlineTemp = element[0]

			element.remove(onlineTemp)

			for res , prot in wmslinks:
				#new val
				for sub in onlineTemp.iter():
					if 'URL' in sub.tag:
						sub.text=res
					if 'name' in sub.tag:
						sub[0].text=layer

				print ET.dump(onlineTemp)
				
				strxml = ET.tostring(onlineTemp).replace("OGC:WMS",prot)

				element.append( ET.fromstring(strxml) )
		if "MD_DataIdentification" in element.tag:
			
			#todo count lelements
			count = 5
			#print  
			#for c in element.getchildren():
			#	print c
			for kw in keywords:
				addKeyword(element,kw,count)		
				
def replace_gmd_gco_gsl(fileName,
	title,
	abstract,
	keywords,
	summary, 
	institution, 
	in_var_institution, 
	contact_email_1, 
	revision_date,
	coverage_start,
	coverage_end,
	geospatial_lat_min="90",
	geospatial_lat_max="-90",
	geospatial_lon_min="-45",
	geospatial_lon_max="45",
	incriment="11000"
	):

	fo = open(fileName,"r+")

	old = fo.read()

	#print geospatial_lon_max
	#print geospatial_lon_min
	#print geospatial_lat_min
	#print geospatial_lat_max

	#.replace("ns0","gmd")\
	#.replace("ns2","gco")\
	#.replace("ns3","gml")\
	#.replace("ns4","gmx")\
	#.replace("TITLE_VARIABLE_CHANGE",title)\


	str1 = old.replace("TITLE_VARIABLE_CHANGE",title)\
		.replace("TITLE_VARIABLE_CHANGE",title)\
		.replace("ABSTRACT_VARIABLE",abstract)\
		.replace("KEYWORD_VARIABLE",str(keywords))\
		.replace("INSTITUTION_VAR",institution)\
		.replace("CONTACT_EMAIL_1_VAR",contact_email_1)\
		.replace("CREATION_DATE_VAR",revision_date)\
		.replace("VAR_INSTITUTION_ID_VAR",in_var_institution)\
		.replace("2011-11-11",coverage_start)\
		.replace('2012-12-12',coverage_end)\
		.replace('geospatial_lat_min', str(geospatial_lat_min))\
		.replace('geospatial_lat_max', str(geospatial_lat_max))\
		.replace('geospatial_lon_min', str(geospatial_lon_min))\
		.replace('geospatial_lon_max', str(geospatial_lon_max))\
		.replace('\n','')\
		.replace('11000',incriment)
	'''
	str1 = str([ fileName,
		title,
		abstract,
		keywords,
		summary, 
		institution, 
		in_var_institution,
		contact_email_1,
		revision_date,
		coverage_start,
		coverage_end, 
		geospatial_lat_min, 
		geospatial_lat_max, 
		geospatial_lon_min, 
		geospatial_lon_max])
	'''
	#root = ET.fromstring(str1)

	# verbouse print.
	#print str1

	#indent(root)
	xmlf = xml.dom.minidom.parseString(str1)
	pretty_xml_as_string = xmlf.toprettyxml()
	#ET.dump(root)

	fo.seek(0,0)

	#fo.write(ET.tostring(root))
	fo.write(pretty_xml_as_string)
	fo.truncate()
	fo.close()

# from net
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i