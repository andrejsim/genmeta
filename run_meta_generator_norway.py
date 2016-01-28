# create all meta
import parse_c4i_catalog
import clipc_metadata_wizard

# generates metadata inspire compliant xmls
# output: metadata dir

#climate4impact catalogue used to extract clipc meta
#catalog_url      = 'http://opendap.knmi.nl/knmi/thredds/catalog/CLIPC/tier1_indicators/icclim_cerfacs/catalog.xml'
#catalog_url_head = "http://opendap.knmi.nl/knmi/thredds/catalog/CLIPC/tier1_indicators/icclim_cerfacs/"
catalog_url_head = "http://thredds.met.no/thredds/dodsC/"
catalog_url_proj = "arcticdata/met.no/CLIPC"
catalog_url      = catalog_url_head+catalog_url_proj

# template based on inspire compliant metadata xml used.
# 
template_inspire_metadata = 'xml.template_inspire_metadata'

target = "metadata/"

count = 0

# http://thredds.met.no/thredds/catalog/arcticdata/met.no/catalog.xml
# this may change...
jname = catalog_url+"/catalog.xml"
title= (catalog_url_proj.replace("/","_").replace(".","_"))
print " cat:   ", jname
print " tit:   ", title 

#def createCSW2( template_xml, opendap , c4iurl, template_xmlNew, title ):

layers = [''];

for layer in layers:
	clipc_metadata_wizard.createCSW2( 	template_xml=template_inspire_metadata, 
										opendap=catalog_url_head, 
										url=jname, 
										template_xmlNew=target+title+"_"+layer+".xml",
										title=title,
										layer=layer )
	

print "end."	