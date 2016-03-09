# python
# knmi clipc
# author: andrej
# clipc@knmi.nl
# 
# validate netcdf global attribute fields in netcdfs
#
import netCDF4
#import urllib2
#from html_table_parser import HTMLTableParser
from lxml import html
import requests
import get_acdd_data

print "clipc netcdf header validator"

# dict
#headers = []
#f = open('clipc.ncdf.headers.list', 'r')
#headers = f.read().split('\n')	
#f.close()

# headers identified at toulouse meta workshop
headers = ['title', 'tier', 'keywords', 'method', 'software', 'software_version', 'software_platform', 'software_project', 'software_reference', 'platform', 'algorithm', 'sensor', 'institution', 'institution_url', 'contact_email', 'summary', 'time_coverage_start', 'time_coverage_end', 'time_coverage_resolution', 'time_coverage_duration', 'cdm_datatype', 'domain', 'geospatial_lat_resolution', 'geospatial_lon_resolution', 'geospatial_lat_min', 'geospatial_lat_max', 'geospatial_lon_min', 'geospatial_lon_max', 'geospatial_bounds', 'conventions', 'date_created', 'creator_name', 'creator_url', 'creator_email', 'project', 'frequency', 'frequency tag', 'history', 'comment', 'standard_name_vocabulary', 'in_var_model_id', 'in_var_project_id', 'in_var_institution_id', 'in_var_model_version_id', 'in_var_driving_model_id', 'in_var_driving_ensemble_member', 'in_var_driving_model_version_id', 'in_var_driving_experiment_id', 'in_var_domain', 'in_var_reference']

#print headers;

# cf convention parametars required in header
#### http://wiki.esipfed.org/index.php/Category:Attribute_Conventions_Dataset_Discovery ###
#http://www.unidata.ucar.edu/software/thredds/current/netcdf-java/metadata/DataDiscoveryAttConvention.html
#acdd_url = "http://wiki.esipfed.org/index.php/Attribute_Convention_for_Data_Discovery#Highly_Recommended"


acdd_dict = get_acdd_data.dictionary()

print acdd_dict.keys()

# TODO
# ADD CF-STANDARDNAME CHECK FOR VARIABLE


# observation parametars required in header
# http://cci.esa.int/sites/default/files/CCI_Data_Requirements_Iss1.2_Mar2015.pdf

# validate variable standard name...
# http://cfconventions.org/Data/cf-standard-names/30/src/cf-standard-name-table.xml

def validate(netcdf_file_url):

	nc = netCDF4.Dataset(netcdf_file_url,'r')

	# global variables tested
	for a in headers:
		if a not in nc.ncattrs():
			print "clipc required: ",a
			

	for a in acdd_dict['Highly Recommended'].keys():
		if a not in nc.ncattrs():
			print "acdd Highly_Recommended: ",a
				
	for a in acdd_dict['Recommended'].keys():
		if a not in nc.ncattrs():
			print "acdd Recommended: ",a
	
	for a in acdd_dict['Suggested'].keys():
		if a not in nc.ncattrs():
			print "acdd Suggested: ",a		

	# variable attributes tested		
	variables = nc.variables.items()
	for k, v in variables:

		# TODO
		# ADD CF-STANDARDNAME CHECK FOR VARIABLE

				# #print k
				# if 'standard_name' not in v.ncattrs(): print k , 'needs standard_name'
				# if 'long_name' not in v.ncattrs(): print k , 'needs long_name'
				# if 'units' not in v.ncattrs(): print k , 'needs units'
				# #if 'grid_mapping' in v.ncattrs():
				# #	if 'standard_name' not in v.ncattrs():
		for varattr in acdd_dict['Highly Recommended Variable Attributes'].keys():		
			if varattr not in v.ncattrs(): print k,' missing acdd: Highly Recommended Variable Attributes ',varattr 


cerfacsfile = "http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tier1_indicators/icclim_cerfacs/vDTR/MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1/vDTR_SEP_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_EUR-11_2006-2100.nc" 

print "CERFACS vdtr dataset"
print cerfacsfile
validate(cerfacsfile)


luisfile = "data/NETCDF4_flooding_1970-01-01T00_33_26Z.nc"
print "PIK flooding dataset"
print luisfile
validate(luisfile)

jrcfile = "data/MER01_ENV01_19980101_19981231_L4_PHE_000003_580N710N0190E0320E_PLC_1200M_PRO.nc"
print "JRC land dataset"
print jrcfile
validate(jrcfile)


tudofile = 'http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/tudo/tier2/WET_LUI_2010-2050.nc'
print "TUDO land dataset"
print tudofile
validate(tudofile)
