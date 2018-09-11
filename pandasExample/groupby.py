import pandas as pd
import numpy as np
import os, sys
from os.path import devnull

old_out = sys.stdout
dev_null = open(devnull, "w")
sys.stdout = dev_null

x0 = pd.Series(np.random.randint(1, 5, 100, np.int))
x1 = pd.Series(np.random.randint(1, 3, 100, np.int))
x2 = pd.Series(np.random.uniform(2, 4, 100))

d = {'x0':x0,
	'x1':x1,
	'x2':x2
	}

df = pd.DataFrame(d)
print df

groupby_x0 = df.groupby(['x0']).median()
print groupby_x0

print df.columns

groupby_x01 = df.groupby(['x0', 'x1']).size()
print groupby_x01

groupby_x01 = df.groupby(['x0', 'x1']).count()
print groupby_x01

groupby_x01 = df.groupby(['x0', 'x1']).mean()
print groupby_x01


groupby_x01 = df.groupby(['x0', 'x1'], axis='index').median()
print groupby_x01

with open(r'/path_to_data/data.csv', "rb") as infile , \
	open(r'/path_to_data/dataSanitized.csv', "wb+") as outfile:
	data = infile.read()
	data = data.replace("[", "").replace("]", "")
	outfile.write(data)
infile.close()
outfile.close()
if 0:
	df_csv = pd.read_csv("file:///path_to_data/dataSanitized.csv", names = ['x0', 'x1', 'x2'], comment = "#")
	
	groupby_x0 = df_csv.groupby(['x0'])
	
	sys.stdout = old_out
	
	print groupby_x0.groups
	print groupby_x0.median()
	print groupby_x0.get_group(1)['x2'].median()
	print groupby_x0.get_group(2)['x2'].median()
	print groupby_x0.get_group(3)['x2'].median()
	
	
	print df_csv.groupby(['x0', 'x1']).median()
	print df_csv.groupby(['x0', 'x1']).median().loc[1]
	print df_csv.groupby(['x0', 'x1']).median().loc[2]
	print df_csv.groupby(['x0', 'x1']).median().loc[3]
	
	print df_csv.groupby(['x0', 'x1']).median().loc[1].loc[7]
	print df_csv.groupby(['x0', 'x1']).median().loc[1].loc[8]
	print df_csv.groupby(['x0', 'x1']).median().loc[1].loc[9]
	print df_csv.groupby(['x0', 'x1']).median().loc[1].loc[10]
	
	print df_csv.groupby(['x0', 'x1']).median().loc[2].loc[7]
	print df_csv.groupby(['x0', 'x1']).median().loc[2].loc[8]
	print df_csv.groupby(['x0', 'x1']).median().loc[2].loc[9]
	print df_csv.groupby(['x0', 'x1']).median().loc[2].loc[10]
	
	print df_csv.groupby(['x0', 'x1']).median().loc[3].loc[7]
	print df_csv.groupby(['x0', 'x1']).median().loc[3].loc[8]
	print df_csv.groupby(['x0', 'x1']).median().loc[3].loc[9]
	print type(df_csv.groupby(['x0', 'x1']).median().loc[3].loc[10])
	print (df_csv.groupby(['x0', 'x1']).median().loc[3].loc[10])
	print (df_csv.groupby(['x0', 'x1']).median().loc[3].loc[10])['x2']
else:
	df_csv = pd.read_csv("file:///path_to_data/dataSanitized.csv", names = ['x0', 'x1', 'x2', 'x3'], comment = "#")
	df_csv['x3'] = df_csv['x3'].str.strip()
	
	groupby_x3 = df_csv.groupby(['x3'])
	
	sys.stdout = old_out
	
	print groupby_x3.groups
	print groupby_x3.get_group('"Berlin"')
	print groupby_x3.get_group('"Berlin"')['x1']
	print "median: ", groupby_x3.get_group('"Berlin"')['x1'].median()
	print groupby_x3.median()