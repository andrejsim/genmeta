# create all meta
import parse_c4i_catalog
import clipc_metadata_wizard

# generates metadata inspire compliant xmls
# output: metadata dir

#climate4impact catalogue used to extract clipc meta
catalog_url = "http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tudo/tier2/"
project_url = "CLIPC/tudo/tier2/catalog.xml"

# template based on inspire compliant metadata xml used.
# 
template_inspire_metadata = 'xml.template_inspire_metadata'

target = "metadata3/"

tudo = ["AGR_LUI_2010-2050.nc","ICS_LUI_2010-2050.nc","NAL_LUI_2010-2050.nc","UGL_LUI_2010-2050.nc","WAT_LUI_2010-2050.nc","FTW_LUI_2010-2050.nc","INF_LUI_2010-2050.nc","NEC_LUI_2020-2050.nc","URB_LUI_2010-2050.nc","WET_LUI_2010-2050.nc"]

links = []
for t in tudo:
	layer = t.split("_")[0]
	nclink = catalog_url+t
	links.append( [layer, nclink] )

for layer,netcdf in links:
	#	print count
	#	print i
	#	if(count > 1 ):
	#		print layer[count-1]
	#		for j in parse_c4i_catalog.readcatalog2B(catalog_url,i):
	name =  netcdf.replace("http://opendap.knmi.nl/knmi/thredds/dodsC/","")\
			.replace(".nc","")\
			.replace("/","_")\
			.replace("-","_")

	print "   ", netcdf
	print "   ", layer
	print "   ", name

				# activate for live generation...
	clipc_metadata_wizard.createCSW4(template_inspire_metadata, catalog_url , [str(netcdf)], target+name+".xml", layer , name )

print "end."	

