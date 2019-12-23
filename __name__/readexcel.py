import pandas as pd

from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('airquality.xlsx')
print(df.columns)
