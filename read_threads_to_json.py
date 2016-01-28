# CLIPC project
# extract metadata from thredds catalogs
# push to mongodb

# author andrej@knmi.nl
import parse_c4i_catalog
import collections
import json

c4i_thredds_catalog      = 'http://opendap.knmi.nl/knmi/thredds/'
c4i_tire1_proj 			 = "CLIPC"

metno_thredds_catalog    = "http://thredds.met.no/thredds/"
metno_proj 				 = "arcticdata/met.no/CLIPC"

data = collections.OrderedDict()

print c4i_thredds_catalog
parse_c4i_catalog.readThreddsCatalog( c4i_thredds_catalog, c4i_tire1_proj,data)

print metno_thredds_catalog
parse_c4i_catalog.readThreddsCatalog( metno_thredds_catalog, metno_proj,data)



output_name = 'thredds.output'
print 'write output to ',output_name

# save as json
outputFile = open( output_name,'w')
outputFile.write( json.dumps(data, indent=4))
outputFile.close()

# read as json
with open( output_name, 'r') as readFile:
	json_doc = readFile.read()
	my_ordered_dict = json.loads( json_doc , object_pairs_hook=collections.OrderedDict)
	readFile.close()

	# display
	for k,v in my_ordered_dict.items():
		print k
		for l in v:
			print "  ",l