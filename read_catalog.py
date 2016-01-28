# python class

class ReadCatalog:

	def __init__(self, catalog_url , project_url):
		self.catalog_url = catalog_url
		self.project_url = project_url
		self.url = catalog_url+project_url+"/catalog.xml"

	def print_list_to_file(self,filename, listOut):
		print 'output to: '+filename
		fileoutlast = open(filename,'w')
		fileoutlast.seek(0,0)
		#fileoutlast.write(listOut)
		fileoutlast.writelines( "%s\n" % item for item in listOut )
	    #fileoutlast.truncate()
		fileoutlast.close()

	def printSelf(self):
		print self.catalog_url
		print self.project_url
		print self.url