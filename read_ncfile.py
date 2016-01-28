# read nc file
import netCDF4
import collections
from datetime import date

def return_ncdump_variables(ncs):

	time = date.today()

	description = []
	keywords = []
	summary = []
	institution = []
	in_var_institution = []
	publication_date = time.isoformat()
	contact_email_1 = []
	revision_date = ""

	coverage_start = "1900"
	coverage_end   = "2100"

	geospatial_lat_min= "-45"
	geospatial_lat_max= "45"
	geospatial_lon_min= "-90"
	geospatial_lon_max= "90"

	in_var_ordereddict = collections.OrderedDict()
	#in_var_key_order = []

	for i in ncs:

		nc_fid = netCDF4.Dataset( i,'r')

		k = 'KEYWORD'
		for j in nc_fid.ncattrs():
			des = nc_fid.getncattr(j)
			if 'description' in j:
				if not des in description:
					description.append(des)
			if 'keywords' in j:
				kwds = des.split(',')
				k = kwds[2]
				for kwd in kwds:
					if not kwd in keywords:
						keywords.append(kwd)
			if 'summary' in j:
				if not des in summary:
					summary.append(des)
			if 'driving_experiment' == j:
				#for item in des:
				print summary
				for item in des.replace(' ','').split(','):
					#print item
					if not item in summary :
						summary.append(item)		
			 		#description.append(des)				
			if 'institution' in j:
				if not des in institution:
					institution.append(des)	
			#if 'in_var_institution' in j:
			if 'in_var_' in j:
				if not des in in_var_institution:
					key = j.replace('in_var_','')
					#in_var_institution.append(des)
					#in_var_key_order.append(key)
					in_var_ordereddict[key] = des	
			if 'project_id' in j:
				if not des in keywords:
						keywords.append(des)	
			if 'experiment_id' in j:
				if not des in keywords:
						keywords.append(des)						
			#if 'contact_email_1' in j:
			if 'contact' in j:	
				if not des in contact_email_1:
					contact_email_1.append(des)		
			if 'version' == j:
				revision_date = des	
			if 'bc_period' in j:
				try:
					coverage_start = des.split("-")[0]
					coverage_end   = des.split("-")[1]	
				except Exception, e:
					coverage_start = "2006"
					coverage_end   = "2100"	
	
			if 'coverage_start' in j:
				coverage_start = des
			if 'coverage_end' in j:
				coverage_end = des		
			if 'geospatial_lat_min' in j:
				geospatial_lat_min= des
			if 'geospatial_lat_max' in j:
				geospatial_lat_max= des	
			if 'geospatial_lon_min' in j:
				geospatial_lon_min= des
			if 'geospatial_lon_max' in j:
				geospatial_lon_max= des
						

	# variable layer parsed for extra info...	

	try:
		layer = nc_fid.variables[k]	
	except:
		for k ,v in nc_fid.variables.items():
			if 'coordinates' in v.ncattrs():
				layer =  nc_fid.variables[k]
				break
	
	# add variable discriptions as keywords	
	try:
		keywords.append(k)
		keywords.append(layer.standard_name)
		keywords.append(layer.long_name)
		keywords.append(layer.units)				
	except Exception, e:
		raise e				

	#print keywords

	in_var_institution = ""
	for k,v in in_var_ordereddict.items():
			in_var_institution = in_var_institution + k +": " + v+ ', \n'

	return ( description \
		, keywords \
		, summary \
		, institution\
		, in_var_institution\
		, contact_email_1\
		, revision_date\
		, coverage_start\
		, coverage_end\
		, geospatial_lat_min\
		, geospatial_lat_max\
		, geospatial_lon_min\
		, geospatial_lon_max\
		)

# end
