import pandas as pd 
from matplotlib import pyplot as plt

df = pd.read_excel('../graphe_problems.xlsx')
df = df.drop(columns = ['Number of different frequency', 'Max frequency'])
print(df.columns)

abr = {'Number of messages sent':'MS', 'Execution time (in ms)':'ET', 'Size of information':'IS'}

#plot per instance
for crit in ['Number of messages sent', 'Execution time (in ms)', 'Size of information']:
	plt.figure()
	for i in [0,2,3,5,6]:
		scen = df[df['Problem']=='scen0{}'.format(i)]
		plt.plot(scen['Algorithm'], scen[crit], 'o', label='scen0{}'.format(i))

	plt.yscale('log')
	plt.grid()
	plt.xlabel('Algorithm')
	plt.ylabel(crit)
	plt.title(crit + '(SCEN0{})'.format(i))
	plt.legend()
	plt.savefig('../plots/scen_{}.png'.format(abr[crit]))

#plot per algo
for crit in ['Number of messages sent', 'Execution time (in ms)', 'Size of information']:
	plt.figure()
	for algo in ['DSA', 'MGM', 'MaxSum', 'ADOPT', 'DPOP']:
		algorithm = df[df['Algorithm']==algo]
		plt.plot(algorithm['Problem'], algorithm[crit], 'o', label=algo)

	plt.yscale('log')
	plt.grid()
	plt.xlabel('Instance')
	plt.ylabel(crit)
	plt.title(crit)
	plt.legend()
	plt.savefig('../plots/algo_{}.png'.format(abr[crit]))