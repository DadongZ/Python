#matplotlib – data visualization
#NumPy – numerical data functionality
#OpenPyXL – read/write Excel 2010 xlsx/xlsm files
#pandas – data import, clean-up, exploration, and analysis
#xlrd – read Excel data
#xlwt – write to Excel
#XlsxWriter – write to Excel (xlsx) files

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', None)

excel_file = '../data/movies.xls'
movies1 = pd.read_excel(excel_file, sheet_name = 0, index_col= 0)
movies2 = pd.read_excel(excel_file, sheet_name = 1, index_col= 0)
movies3 = pd.read_excel(excel_file, sheet_name = 2, index_col= 0)

movies = pd.concat([movies1, movies2, movies3])
print(movies.shape)
print(movies.head)

sorted_by_gross = movies.sort_values(['Gross Earnings'], ascending=False)
print(sorted_by_gross.head(10))

sorted_by_gross['Gross Earnings'].head(10).plot(kind='barh')

plt.show()