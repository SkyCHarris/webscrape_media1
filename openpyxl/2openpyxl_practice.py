import openpyxl

wb = openpyxl.load_workbook("balance.xlsx")
ws = wb['Sheet1']

# Use .value method to print contents of cell
print(ws['B5'].value)

# Use .cell method to print contents of cell by rows/columns #
print(ws.cell(row=6, column=1).value)

# Pass multiple cell contents
#? Need to unpack nested tuple to extract each value
value_range = ws['A2' : 'B5']

for a, b in value_range:
    print(a.value, b.value)