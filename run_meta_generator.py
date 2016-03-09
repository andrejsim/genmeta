# create all meta
import parse_c4i_catalog
import clipc_metadata_wizard

# generates metadata inspire compliant xmls
# output: metadata dir

#climate4impact catalogue used to extract clipc meta
catalog_url = "http://opendap.knmi.nl/knmi/thredds/catalog/"
project_url = "CLIPC/tier1_indicators/icclim_cerfacs/catalog.xml"

# template based on inspire compliant metadata xml used.
# 
template_inspire_metadata = 'xml.template_inspire_metadata'

target = "metadata/"

count = 0
(layer , links) = parse_c4i_catalog.readcatalogB(catalog_url,project_url)


for i in links:
	print count
	print i
	if(count > 1 ):
		print layer[count-1]
		for j in parse_c4i_catalog.readcatalog2B(catalog_url,i):
			jname =  j.replace("http://opendap.knmi.nl/knmi/thredds/catalog/CLIPC/tier1_indicators/icclim_cerfacs/","")\
			.replace("/catalog.xml","")\
			.replace("/","_")\
			.replace("-","_")

			print "   ", jname

			# activate for live generation...
			clipc_metadata_wizard.createCSW(template_inspire_metadata, catalog_url , j, target+jname+".xml",layer[count-1],jname)
	count += 1	

print "end."	

