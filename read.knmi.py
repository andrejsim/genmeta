# read met.no 
import parse_c4i_catalog
from read_catalog import ReadCatalog


class ReadKNMI(ReadCatalog):

	def __init__(self):
		catalog_url_head = "http://opendap.knmi.nl/knmi/thredds/catalog/"
		catalog_url_proj = "CLIPC/tier1_indicators/icclim_cerfacs"

		catalog_url      = catalog_url_head+catalog_url_proj+"/catalog.xml"

		wmsStart = 'https://climate4impact.eu/impactportal/ImpactService?source='
		#catalog = 'http://opendap.knmi.nl/knmi/thredds/catalog/'
		opendap = 'http://opendap.knmi.nl/knmi/thredds/dodsC/'
		wmsEnd = '&service=WMS&'



		ReadCatalog.__init__(self , catalog_url_head ,catalog_url_proj)


		print catalog_url

		links , ncs = parse_c4i_catalog.readcatalog4(catalog_url,opendap,wmsStart,wmsEnd )

		self.print_list_to_file('knmi.wms',links)
		self.print_list_to_file('knmi.ncs',ncs)

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
			line = n.split('/')[11].split('_')
			print line
			if line[0] not in uni['variable']:
				uni['variable'].append(line[0])
			elif line[2] not in uni['model']:
				uni['model'].append(line[2])	
			elif line[3] not in uni['experiment']:
				uni['experiment'].append(line[3])	
			elif line[4] not in uni['ensemble']:
				uni['ensemble'].append(line[4])
			elif line[5] not in uni['regional']:
				uni['regional'].append(line[5])	
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


catalogKNMI = ReadKNMI()		