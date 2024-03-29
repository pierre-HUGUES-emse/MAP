#import xml.etree.ElementTree as ET
import sys

def parse(scen):
	base_path = "../FullRLFAP/CELAR/"
	output_file = "../problems_xml/" + scen + "Output.xml"

	var_tab2 = []
	ctr_tab2 = []
	dom_tab2 = []
	cst_tab2 = []
	costs=[0]*8

	with open(base_path + scen + '/var.txt', 'r') as var_file:
		var = var_file.read()
		var_tab = var.split("\n")
		for i, j in enumerate(var_tab[:-1]):
			var_tab2.append(list(map(int, j.split())))

	with open(base_path + scen + '/ctr.txt', 'r') as ctr_file:
		ctr = ctr_file.read()
		ctr_tab = ctr.split("\n")
		for i, j in enumerate(ctr_tab[:-1]):
			j = j.split()
			try:
				ctr_tab2.append([int(j[0]), int(j[1]), str(j[3]), int(j[4]), int(j[5])])
			except:
				ctr_tab2.append([int(j[0]), int(j[1]), str(j[3]), int(j[4]), -1])


	with open(base_path + scen + '/dom.txt', 'r') as dom_file:
		dom = dom_file.read()
		dom_tab = dom.split("\n")
		for i, j in enumerate(dom_tab[:-1]):
			dom_tab2.append(j.split())

	with open(base_path + scen + '/cst.txt', 'r') as cst_file:
		cst = cst_file.read()
		cst_tab = cst.split("\n")
		for i, j in enumerate(cst_tab[:-1]):
			cst_tab2.append(j)
		if '' in cst_tab2:
			cst_tab3 = cst_tab2[cst_tab2.index('')+1:]
			for k in range(len(cst_tab3)):
				costs[k] = cst_tab3[k].split()[2]

	nb_agent = len(var_tab2)

	with open(output_file, 'w') as output_file:
		#instance = ET.Element('instance')
		#	s = '<?xml version="1.0" encoding="UTF-8"?>\n'
		s = '<instance>\n'
		#s += 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="src/frodo2/algorithms/XCSPschemaJaCoP.xsd">\n'
		s += '\t<presentation name="{}" maxConstraintArity="2" maximize="false" format="XCSP 2.1_FRODO"/>\n'.format(scen)
		s += '\t<agents nbAgents="{}">\n'.format(nb_agent)
		
		for i in range(nb_agent):
			s += '\t\t<agent name="agent_{}"/>\n'.format(i)
		
		s += "\t</agents>\n"
		s += '\t<domains nbDomains="{}">\n'.format(len(dom_tab2))
		
		for i in range(len(dom_tab2)):
			s += '\t\t<domain name="{}" nbValues="{}">{}</domain>\n'.format(dom_tab2[i][0], dom_tab2[i][1], ' '.join(dom_tab2[i][2:]))
		
		s += '\t</domains>\n'
		s += '\t<variables nbVariables="{}">\n'.format(len(var_tab2))
		
		for i in range(len(var_tab2)):
			s += '\t\t<variable name="{}" domain="{}" agent="{}"/>\n'.format(var_tab2[i][0], var_tab2[i][1], 'agent_'+str(i))

		s += '\t</variables>\n'
		s += '\t<predicates nbPredicates="2">\n'
		s += '\t\t<predicate name="EQ">\n'
		s += '\t\t\t<parameters> int F1 int F2 int K12 int C</parameters>\n'
		s += '\t\t\t<expression>\n'
		s += '\t\t\t\t<functional> if(eq(abs(sub(F1,F2)), K12), 0, C) </functional>\n'
		s += '\t\t\t</expression>\n'
		s += '\t\t</predicate>\n'
		s += '\t\t<predicate name="SUP">\n'
		s += '\t\t\t<parameters> int F1 int F2 int K12 int C</parameters>\n'
		s += '\t\t\t<expression>\n'
		s += '\t\t\t\t<functional> if(gt(abs(sub(F1,F2)), K12), 0, C) </functional>\n'
		s += '\t\t\t</expression>\n'
		s += '\t\t</predicate>\n'
		s += '\t</predicates>\n'

		s += '\t<constraints nbConstraints="{}">\n'.format(len(ctr_tab2))
		for i in range(len(ctr_tab2)):
			if ctr_tab2[i][4] == 0:
				list_ctr =  [str(ctr_tab2[i][0]), str(ctr_tab2[i][1]), str(ctr_tab2[i][3]), str(100*int(costs[0]))]
			elif ctr_tab2[i][4] == -1:
				list_ctr =  [str(ctr_tab2[i][0]), str(ctr_tab2[i][1]), str(ctr_tab2[i][3]), str(1)]
			else:
				list_ctr =  [str(ctr_tab2[i][0]), str(ctr_tab2[i][1]), str(ctr_tab2[i][3]), str(costs[ctr_tab2[i][4]])]
			dic = {'=':'EQ', '>':'SUP'}
			s += '\t\t<constraint name="{}" arity="2" scope="{}" reference="{}">\n'.format(str(i), ' '.join(list_ctr[:-2]), dic[ctr_tab2[i][2]])
			s += '\t\t\t<parameters>{}</parameters>\n'.format(' '.join(list_ctr))
			s += '\t\t</constraint>\n'
		s += '\t</constraints>\n'
		s += '</instance>'

		output_file.write(s)

