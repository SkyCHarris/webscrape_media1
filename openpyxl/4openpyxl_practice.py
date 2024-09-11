# Write/Update Data in Excel

import openpyxl

wb = openpyxl.load_workbook("balance.xlsx")
ws = wb['Sheet1']

# Modify value in B5 cell to something else
ws['B5'].value = 9
wb.save("balance.xlsx")

# Add 2 new values
ws['A9'] = 'Rick'
ws['B9'] = 1500
wb.save("balance.xlsx")

# Read cell contents using .cell method
print(ws.cell(row=5, column=2).value)

# Set cell equal to something new
ws.cell(row=5, column=2).value = 80000
wb.save("balance.xlsx")

# Change multiple values (such as entire row/column)
# Double value of B column and add values to C column

# ws.cell(row=1, column=3).value = 1000
# ws.cell(row=2, column=3).value = 100000
# wb.save("balance.xlsx")

# Title first
# ws['C1'] = 'Double Balance'
# wb.save("balance.xlsx")

# Extract values for B column
for i in range(2,10):   # 2 because we don't want titles
    b_col = ws.cell(row=i, column=2).value  # Get values in B column
    c_values = b_col*2
    ws.cell(row=i, column=3).value = c_values

wb.save("balance.xlsx")

