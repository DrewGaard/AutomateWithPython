import openpyxl

workbook = openpyxl.load_workbook('example.xlsx')

print(type(workbook))

sheet = workbook['Sheet1']

print(str(sheet['A1'].value))

print(str(sheet['C1'].value))

print(sheet.cell(row=1, column=2).value)

for i in range(1, 8):
    print('Cell B' + str(i) + ' contains: ' + str(sheet['B' + str(i)].value))
