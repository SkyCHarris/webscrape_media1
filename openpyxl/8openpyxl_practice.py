# Format Data in Excel

import openpyxl
from openpyxl.styles import numbers

wb = openpyxl.load_workbook("balance.xlsx")
ws = wb['Score']

# Set value for date column
ws['C4'] = '11/11/20'

# Set value for text and number columns
ws['D4'] = 20
ws['E4'].number_format = numbers.FORMAT_TEXT = 'Beginner'   # Bugs out excel for some reason

wb.save("balance.xlsx")