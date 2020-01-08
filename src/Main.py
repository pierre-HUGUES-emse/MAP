from scen_parse import *

if __name__=="__main__":
	scen =[]
	for i in range(12):
		scen.append('scen{0:02d}'.format(i))
	for s in scen:
		parse(s)