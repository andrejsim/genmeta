# python
# inspire fields dict
# map to cerfacs
#
# project: clipc
# author: andrej

from collections import OrderedDict

# http://csw.climate4impact.eu/geonetwork/srv/eng/catalog.search
#
# maping of nc_global to 
# keys=inspire xml fields
# values=netcdf nc_global fields
inspire_fields_dict =   OrderedDict([
						#inspire   			  #nc_global
						('title'				,	'nc_fileName'), # change to human readable format variable # discussed in emails.
						('abstract'				,	'description'),
						('keyword'				, 	['keywords', # tuple distributed according to vocabularies 
											  		'project_id',
											  		'experiment_id',
											  		'standard_name' ]) , # we extract this from the variable and added to the keywords, but the short name changes by user
						('date' 				, 'revision_date'), # day-month-year preffered (publication)
						('organisationName'		, 'institution'),
						('electronicMailAddress', 'contact_email_1'), # alternative contact_email add as tuple [ , ]
						('statement'			, 'in_vars'), # all experiment related data is used in lineage
						('beginPosition'		, 'coverage_start'),
						('endPosition'			, 'coverage_end'),
						('southBoundLatitude'	, 'geospatial_lat_min'),
						('northBoundLatitude'	, 'geospatial_lat_max'),
						('westBoundLongitude'	, 'geospatial_lon_min'),
						('eastBoundLongitude'	, 'geospatial_lon_max'),
						('resolution'			, 'geospatial_increment'), #0.11 degree as 11000 m...
						('?5'					, 'domain') ,
						('?4'					, 'summary')	,			# this could be more relevant... now double
						# we would like to see:
						('?3'					, 'variable'), # layer in netcdf or layer in
						('?2'                 	, 'units'),    # clarify with portal team 
						('?1'					, 'software'), #
						('CRI'					, '?') # based on domain currently... hard coded
						('uncertanty')
						])


list1 = []
for v in inspire_fields_dict.values():
	list1.append(v)	

for l in list1:
	print  str("('"+str(l)+"'	:	''),").replace(' ','')						

# nc_fileName
# description
# keywords
# project_id
# experiment_id
# variable
# variable.standard_name 
# revision_date
# institution
# contact_email_1
# in_vars
# coverage_start
# coverage_end
# geospatial_lat_min
# geospatial_lat_max
# geospatial_lon_min
# geospatial_lon_max
# geospatial_increment
# domain
# summary
# variable
# units
# software

