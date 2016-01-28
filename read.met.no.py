# read met.no 
import parse_c4i_catalog
from read_catalog import ReadCatalog


class ReadMetNo(ReadCatalog):

	def __init__(self):
		catalog_url_head = "http://thredds.met.no/thredds/dodsC/"
		catalog_url_proj = "arcticdata/met.no/CLIPC"
		catalog_url      = catalog_url_head+catalog_url_proj+"/catalog.xml"

		wmsStart = 'http://thredds.met.no/thredds/wms/'#'https://climate4impact.eu/impactportal/ImpactService?source='
		#catalog = 'http://opendap.knmi.nl/knmi/thredds/catalog/'
		#opendap = 'http://opendap.knmi.nl/knmi/thredds/dodsC/'
		wmsEnd = '?service=WMS&version=1.3.0&request=GetCapabilities'



		ReadCatalog.__init__(self , catalog_url_head ,catalog_url_proj)


		layer = ''

		links , ncs = parse_c4i_catalog.readcatalog3B(catalog_url,catalog_url_head,wmsStart,wmsEnd , layer)

		self.print_list_to_file('met.no.wms',links)
		self.print_list_to_file('met.no.ncs',ncs)

		print len(ncs)

		#class UniDict():

		print ""

		uni = {}
		uni['variable'] = []
		uni['experiment'] = []
		uni['model'] = []
		uni['ensemble'] = []
		uni['regional'] = []
		#uni['8'] = []

		for n in ncs:
			line = n.split('_')
			#print line
			if line[1] not in uni['variable']:
				uni['variable'].append(line[1])
			elif line[3] not in uni['model']:
				uni['model'].append(line[3])	
			elif line[4] not in uni['experiment']:
				uni['experiment'].append(line[4])	
			elif line[5] not in uni['ensemble']:
				uni['ensemble'].append(line[5])
			elif line[6] not in uni['regional']:
				uni['regional'].append(line[6])	
			#elif line[8] not in uni['8']:
			#	uni['8'].append(line[8])

		for k in uni.keys():
			print k+": "+str(uni[k])

		print ""
		self.printSelf()

		#fileName = 'ncs.last'
		#fo = open(fileName,"r+")
		#old = fo.read()
		#print old


catalogMetNo = ReadMetNo()		