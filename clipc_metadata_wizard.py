import xml.etree.ElementTree as ET
import generate_metadata_etree
import parse_c4i_catalog
import read_ncfile

def createCSW( template_xml, opendap , c4iurl, template_xmlNew, layer, title ):
	
	#
	tree = ET.parse(template_xml)

	#print ET.dump(tree)
	wmsStart = 'https://climate4impact.eu/impactportal/ImpactService?source='
	#catalog = 'http://opendap.knmi.nl/knmi/thredds/catalog/'
	opendap = 'http://opendap.knmi.nl/knmi/thredds/dodsC/'
	wmsEnd = '&service=WMS&'
	#

	links , ncs = parse_c4i_catalog.readcatalog3(c4iurl,opendap,wmsStart,wmsEnd)

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
	
	#
	tree = ET.parse(template_xml)

	#print ET.dump(tree)
	wmsStart = 'http://thredds.met.no/thredds/wms'#'https://climate4impact.eu/impactportal/ImpactService?source='
	#catalog = 'http://opendap.knmi.nl/knmi/thredds/catalog/'
	#opendap = 'http://opendap.knmi.nl/knmi/thredds/dodsC/'
	wmsEnd = '&service=WMS&request=GetCapabilities'
	#

	print template_xml
	print opendap
	print url
	print template_xmlNew
	print title

	#layer = "tasminAdjust"

	links , ncs = parse_c4i_catalog.readcatalog3B(url,opendap,wmsStart,wmsEnd , layer)

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