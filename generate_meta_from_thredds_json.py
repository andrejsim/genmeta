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


output_name = 'thredds.output'
print 'generate meta from ',output_name

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