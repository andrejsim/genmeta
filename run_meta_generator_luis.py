# create all meta
import parse_c4i_catalog
import clipc_metadata_wizard

# generates metadata inspire compliant xmls
# output: metadata dir

#climate4impact catalogue used to extract clipc meta
catalog_url = "http://opendap.knmi.nl/knmi/thredds/catalog/"
project_url = "CLIPC/pik/Tier2/flood_hist/catalog.xml"

# template based on inspire compliant metadata xml used.
# 
template_inspire_metadata = 'xml.template_inspire_metadata'

target = "metadata2/"

links = [	("flooding" ,"http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/pik/tier2/flood_hist/f_6763.nc" , "pik/tier2/flood_hist")  ,
			("flooding" ,"http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/pik/tier2/flood_v2/f_6763.nc"	  ,	"pik/tier2/flood_v2")    ,
			("flooding" ,"http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/pik/tier2/flood_rcp85/f_6763.nc", "pik/tier2/flood_rcp85") ,
			("MoD" 		,"http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/syke/tier1/MoD/MoD_in_var_CryoLandFSC_2001_2014_Europe.nc","syke/tier1/MoD"),
			("MPI" 		,"http://opendap.knmi.nl/knmi/thredds/dodsC/CLIPC/syke/tier2/MPI/MPI_in_var_MoD_2001_2014_Finland.nc","syke/tier2/MPI") ]

#parse_c4i_catalog.readcatalogB(catalog_url,project_url)

#https://climate4impact.eu/impactportal/adagucviewer/?srs=EPSG%3A3857&bbox=29109.947643979103,6500000,1190890.052356021,7200000&service=https%3A%2F%2Fclimate4impact.eu%2Fcgi-bin%2Fadaguc.clipc.cgi%3F&layer=tier2%2Fpik%2Fflood_v2%24image%2Fpng%24true%24elevation%2Fnearest%241%240&selected=0&dims=time$1970-01-01T00:33:26Z&baselayers=streetmap$ne_10m_admin_0_countries_simplified
#https://climate4impact.eu/impactportal/adagucviewer/?srs=EPSG%3A3857&bbox=29109.947643979103,6500000,1190890.052356021,7200000&service=https%3A%2F%2Fclimate4impact.eu%2Fcgi-bin%2Fadaguc.clipc.cgi%3F&layer=tier2%2Fpik%2Fflood_rcp85%24image%2Fpng%24true%24elevation%2Fnearest%241%240&selected=0&dims=time$1970-01-01T00:33:26Z&baselayers=streetmap$ne_10m_admin_0_countries_simplified
#https://climate4impact.eu/impactportal/adagucviewer/?srs=EPSG%3A3857&bbox=29109.947643979103,6500000,1190890.052356021,7200000&service=https%3A%2F%2Fclimate4impact.eu%2Fcgi-bin%2Fadaguc.clipc.cgi%3F&layer=tier2%2Fpik%2Fflood_hist%24image%2Fpng%24true%24elevation%2Fnearest%241%240&selected=0&dims=time$1970-01-01T00:33:26Z&baselayers=streetmap$ne_10m_admin_0_countries_simplified

for layer,netcdf,dataset in links:
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
	clipc_metadata_wizard.createCSW3(template_inspire_metadata, catalog_url , [str(netcdf)], target+name+".xml", layer , name , dataset)

print "end."	

