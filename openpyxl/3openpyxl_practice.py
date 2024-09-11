# Iterate and Read Rows and Columns

import openpyxl

wb = openpyxl.load_workbook("balance.xlsx")
ws = wb['Sheet1']

#! iter_rows
# Specify column dimensions
iterate_rows = ws.iter_rows(min_row=1, max_row=7, min_col=1, max_col=2)
print(iterate_rows)

# Print generative object values
# for row in iterate_rows:
#     print(row)

# Get contents from cells (instead of tuples)
# for a,b in iterate_rows:
#     print(a.value, b.value)

# Store value in python object to use for further operation
# names = []
# balance = []
# for a,b in iterate_rows:
#     names.append(a.value)
#     balance.append(b.value)

# print(names, balance)


#! iter_cols

iterate_columns = ws.iter_cols(min_row=1, max_row=5, min_col=1, max_col=2)

# Tuple for each column, unpack differently!
# Use
# for a,b in iterate_columns:
#     print(a.value, b.value)

# Extract all rows
print(list(ws.rows))