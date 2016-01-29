# python
# inspire fields dict
# map to cerfacs
#
# project: clipc
# author: andrej

# http://csw.climate4impact.eu/geonetwork/srv/eng/catalog.search
#
# maping of nc_global to 
# keys=inspire xml fields
# values=netcdf nc_global fields
inspire_fields_dict =   {
						#inspire   			  #nc_global
						'title'				: 'nc fileName' # change to human readable format variable # discussed in emails.
						'abstract'			: 'description'
						'keyword'			:['keywords', # tuple distributed according to vocabularies 
											  'project_id',
											  'experiment_id',
											  'standard_name' ] , # we extract this from the variable and added to the keywords, but the short name changes by user
						'date' 				: 'revision_date' # day-month-year preffered
						'organisationName'	: 'institution'
						'electronicMailAddress'	: 'contact_email_1' # alternative contact_email add as tuple [ , ]
						'statement'			: 'in_vars' # all experiment related data is used in lineage
						'beginPosition'		: 'coverage_start',
						'endPosition'		: 'coverage_end',
						'southBoundLatitude': 'geospatial_lat_min',
						'northBoundLatitude': 'geospatial_lat_max',
						'westBoundLongitude': 'geospatial_lon_min',
						'eastBoundLongitude': 'geospatial_lon_max',
						'resolution'		: 'geospatial_increment' #0.11 degree as 11000 m...
						'?'					: 'domain'
						'?'					: 'summary'				# this could be more relevant... now double
						# we would like to see:
						'?'					: 'variable', # layer in netcdf or layer in
						'?'                 : 'units',    # clarify with portal team 
						'?'					: 'software', #
						'CRI'				: '?' # based on domain currently... hard coded
						}