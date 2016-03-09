import xml.etree.ElementTree as ET
import generate_metadata_etree
import parse_c4i_catalog
import read_ncfile

def createCSW( template_xml, opendap , c4iurl, template_xmlNew, layer, title ):
	
	ET.register_namespace("gmd" , "http://www.isotc211.org/2005/gmd")
	ET.register_namespace("gco" , "http://www.isotc211.org/2005/gco")
	ET.register_namespace("gmx" , "http://www.isotc211.org/2005/gmx")
	ET.register_namespace("gml" , "http://www.opengis.net/gml/3.2")
	ET.register_namespace("xlink","http://www.w3.org/1999/xlink")
	#
	tree = ET.parse(template_xml)

	#print ET.dump(tree)
	WS_start = 'https://climate4impact.eu/impactportal/ImpactService?source='
	#catalog = 'http://opendap.knmi.nl/knmi/thredds/catalog/'
	opendap = 'http://opendap.knmi.nl/knmi/thredds/dodsC/'
	WS_end = '&service=WMS&'
	#

	links , ncs = parse_c4i_catalog.readcatalog3(c4iurl,opendap,WS_start,WS_end)

	( description\
		, keywords\
		, summary\
		, institution\
		, in_var_institution\
		, contact_email_1\
		, revision_date \
		, coverage_start \
		, coverage_end\
		, geospatial_lat_min\
		, geospatial_lat_max\
		, geospatial_lon_min\
		, geospatial_lon_max ) = read_ncfile.return_ncdump_variables(ncs)

	generate_metadata_etree.replace_onlineResource(tree,ncs,links,layer,keywords)

	#print type(tree)
	#print ET.dump(tree)


	#for elem in tree.getiterator():
    #	print elem.tag , elem.attrib


	tree.write( template_xmlNew, method="xml")

	#print summary
	#print keywords

	# write metadata to file...
	generate_metadata_etree.replace_gmd_gco_gsl(template_xmlNew,
		title,
		description[0],
		keywords,
		summary[0], 
		institution[0], 
		in_var_institution,
		contact_email_1[0],
		revision_date,
		coverage_start,
		coverage_end, 
		geospatial_lat_min, 
		geospatial_lat_max, 
		geospatial_lon_min, 
		geospatial_lon_max)


def print_last_to_file(filename, listOut):
	fileoutlast = open(filename,'w')
	fileoutlast.seek(0,0)
	#fileoutlast.write(listOut)
	fileoutlast.writelines( "%s\n" % item for item in listOut )
    #fileoutlast.truncate()
	fileoutlast.close()


def createCSW2( template_xml, opendap , url, template_xmlNew, title , layer):
	
	ET.register_namespace("gmd" , "http://www.isotc211.org/2005/gmd")
	ET.register_namespace("gco" , "http://www.isotc211.org/2005/gco")
	ET.register_namespace("gmx" , "http://www.isotc211.org/2005/gmx")
	ET.register_namespace("gml" , "http://www.opengis.net/gml/3.2")
	ET.register_namespace("xlink","http://www.w3.org/1999/xlink")

	tree = ET.parse(template_xml)

	#print ET.dump(tree)
	WS_start = 'http://thredds.met.no/thredds/wms'#'https://climate4impact.eu/impactportal/ImpactService?source='
	#catalog = 'http://opendap.knmi.nl/knmi/thredds/catalog/'
	#opendap = 'http://opendap.knmi.nl/knmi/thredds/dodsC/'
	WS_end = '&service=WMS&request=GetCapabilities'
	#

	print template_xml
	print opendap
	print url
	print template_xmlNew
	print title

	#layer = "tasminAdjust"

	links , ncs = parse_c4i_catalog.readcatalog3B(url,opendap,WS_start,WS_end , layer)

	print_last_to_file("wms.last",links)
	print_last_to_file("ncs.last",ncs)

	( description\
		, keywords\
		, summary\
		, institution\
		, in_var_institution\
		, contact_email_1\
		, revision_date \
		, coverage_start \
		, coverage_end\
		, geospatial_lat_min\
		, geospatial_lat_max\
		, geospatial_lon_min\
		, geospatial_lon_max ) = read_ncfile.return_ncdump_variables(ncs)

	#print tree
	#print keywords
	#print in_var_institution
	
	generate_metadata_etree.replace_onlineResource(tree,ncs,links,layer,keywords)

	tree.write( template_xmlNew, method="xml")

	#print 'summary'
	#print str(summary)
	#print 'keywords'
	#print keywords

	# write metadata to file...
	generate_metadata_etree.replace_gmd_gco_gsl(template_xmlNew,
		title,
		str(description),
		keywords,
		summary[0], 
		institution[0], 
		str(in_var_institution),
		contact_email_1[0],
		revision_date,
		coverage_start,
		coverage_end, 
		geospatial_lat_min, 
		geospatial_lat_max, 
		geospatial_lon_min, 
		geospatial_lon_max)


# 
#i_template_xml = '/usr/people/mihajlov/geonetworks/metadata.geonet.temp.vdtr.xml'
#i_c4iurl = 'http://opendap.knmi.nl/knmi/thredds/catalog/CLIPC/tier1_indicators/icclim_cerfacs/vDTR/EURO4M_MESANv1/catalog.xml'
#i_template_xmlNew = '/usr/people/mihajlov/geonetworks/metadata.B.xml'
#createCSW( i_template_xml, i_c4iurl, i_template_xmlNew)
#

#http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tier1_indicators/icclim_cerfacs/TXn/MPI-M-MPI-ESM-LR_rcp45_r1i1p1_SMHI-RCA4_v1-SMHI-DBS43-MESAN-1989-2010


def createCSW3( template_xml, opendap , c4iurl, template_xmlNew, layer, title ,dataset):
	
	ET.register_namespace("gmd" , "http://www.isotc211.org/2005/gmd")
	ET.register_namespace("gco" , "http://www.isotc211.org/2005/gco")
	ET.register_namespace("gmx" , "http://www.isotc211.org/2005/gmx")
	ET.register_namespace("gml" , "http://www.opengis.net/gml/3.2")
	ET.register_namespace("xlink","http://www.w3.org/1999/xlink")
	#
	tree = ET.parse(template_xml)


	ncs = c4iurl

	# print ET.dump(tree)
	WCS_start = 'https://climate4impact.eu/cgi-bin/adagucserver.cgi?DATASET=' 
	WMS_start = 'https://climate4impact.eu/cgi-bin/adagucserver.cgi?DATASET='
	#catalog = 'http://opendap.knmi.nl/knmi/thredds/catalog/'
	#opendap = 'http://opendap.knmi.nl/knmi/thredds/dodsC/'
	WCS_end = '&SERVICE=WCS&REQUEST=GetCapabilities'
	WMS_end = '&SERVICE=WMS&REQUEST=GetCapabilities'

	#https://climate4impact.eu/cgi-bin/adagucserver.cgi?DATASET=pik/tier2/flood_rcp85&SERVICE=WMS&REQUEST=GetCapabilities
	#links , ncs = parse_c4i_catalog.readcatalog3(c4iurl,opendap,WS_start,WS_end)

	# add links ...
	links = []
	for link in c4iurl:
		links.append( (WMS_start+dataset+WMS_end,"OGC:WMS"))
		links.append( (WCS_start+dataset+WCS_end,"OGC:WCS"))
		#links.append(WS_start+l+WS_end) 

	print ncs

	( description\
		, keywords\
		, summary\
		, institution\
		, in_var_institution\
		, contact_email_1\
		, revision_date \
		, coverage_start \
		, coverage_end\
		, geospatial_lat_min\
		, geospatial_lat_max\
		, geospatial_lon_min\
		, geospatial_lon_max ) = read_ncfile.return_ncdump_variables(ncs)


	print type(keywords)
	print keywords
	print links[0]

	generate_metadata_etree.replace_onlineResource(tree,ncs,links,layer,keywords)

	#print type(tree)
	#print ET.dump(tree)


	#for elem in tree.getiterator():
    #	print elem.tag , elem.attrib


	tree.write( template_xmlNew, method="xml")

	print summary
	#print keywords


	# write metadata to file...
	generate_metadata_etree.replace_gmd_gco_gsl(template_xmlNew,
		title,
		description[0],
		keywords,
		summary,#summary[0], 
		institution[0], 
		in_var_institution,
		contact_email_1[0],
		revision_date,
		coverage_start,
		coverage_end, 
		geospatial_lat_min, 
		geospatial_lat_max, 
		geospatial_lon_min, 
		geospatial_lon_max,
		incriment="25")


# "http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tudo/tier2/"
def createCSW4( template_xml, opendap , c4iurl, template_xmlNew, layer, title):
	
	ET.register_namespace("gmd" , "http://www.isotc211.org/2005/gmd")
	ET.register_namespace("gco" , "http://www.isotc211.org/2005/gco")
	ET.register_namespace("gmx" , "http://www.isotc211.org/2005/gmx")
	ET.register_namespace("gml" , "http://www.opengis.net/gml/3.2")
	ET.register_namespace("xlink","http://www.w3.org/1999/xlink")
	#
	tree = ET.parse(template_xml)


	ncs = c4iurl

	# https://climate4impact.eu/impactportal/adagucserver?
	# source=http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tudo/tier2/NAL_LUI_2010-2050.nc
	# &service=WMS&request=getcapabilities


	#WMS_start = 'https://climate4impact.eu/cgi-bin/adagucserver.cgi?DATASET='
	WMS_start = 'https://climate4impact.eu/adagucserver?source='
	WMS_end = '&SERVICE=WMS&REQUEST=GetCapabilities'

	# add links ...
	links = []
	for link in c4iurl:
		links.append( (WMS_start+link+WMS_end,"OGC:WMS"))
		#links.append( (WCS_start+dataset+WCS_end,"OGC:WCS"))
		#links.append(WS_start+l+WS_end) 

	print ncs

	( description\
		, keywords\
		, summary\
		, institution\
		, in_var_institution\
		, contact_email_1\
		, revision_date \
		, coverage_start \
		, coverage_end\
		, geospatial_lat_min\
		, geospatial_lat_max\
		, geospatial_lon_min\
		, geospatial_lon_max ) = read_ncfile.return_ncdump_variables(ncs)


	print type(keywords)
	print keywords
	print links[0]

	generate_metadata_etree.replace_onlineResource(tree,ncs,links,layer,keywords)

	#print type(tree)
	#print ET.dump(tree)


	#for elem in tree.getiterator():
    #	print elem.tag , elem.attrib


	tree.write( template_xmlNew, method="xml")

	print summary
	#print keywords


	# write metadata to file...
	generate_metadata_etree.replace_gmd_gco_gsl(template_xmlNew,
		title,
		description[0],
		keywords,
		summary,#summary[0], 
		institution[0], 
		in_var_institution,
		contact_email_1[0],
		revision_date,
		coverage_start,
		coverage_end, 
		geospatial_lat_min, 
		geospatial_lat_max, 
		geospatial_lon_min, 
		geospatial_lon_max,
		incriment="100")