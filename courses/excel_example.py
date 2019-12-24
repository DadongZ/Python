import pandas as pd

excel_file = 'airquality.xlsx'

air = pd.read_excel(excel_file)

air.head()
