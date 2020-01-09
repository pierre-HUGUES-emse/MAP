import xml.etree.ElementTree as ET

def criteria(path):
	tree = ET.parse(path)
	root = tree.getroot()
	values =[]
	for child in root:
		values.append(child.attrib['value'])
	return len(set(values)), max(map(int,values))




paths = []
paths.append('../output/DSA_scen02.xml')
paths.append('../output/MGM_scen02.xml')
paths.append('../output/MaxSum_scen02.xml')
paths.append('../output/MGM_scen03.xml')
paths.append('../output/MaxSum_scen03.xml')
paths.append('../output/DSA_scen03.xml')

for path in paths:
	print(criteria(path))
