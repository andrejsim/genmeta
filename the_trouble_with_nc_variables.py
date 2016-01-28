# test
import netCDF4


nc_url = "http://thredds.met.no/thredds/dodsC/arcticdata/met.no/CLIPC/CLIPC_tasminAdjust_EUR-44_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_METNO-QMAP-EOBS10-1981-2010_day_20760101-20801231.nc"

nc_fid = netCDF4.Dataset( nc_url ,'r')

for k,v in nc_fid.variables.items():
	if 'coordinates' in v.ncattrs():
		print str(k)
		print v.standard_name
		print v.long_name
		print v.units