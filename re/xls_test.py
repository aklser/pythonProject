import xlrd

book = xlrd.open_workbook("income.xls")
# print(book.sheet_names())
# print(book.nsheets)
for i in book.sheets():
    print(i.nrows)
    print(i.ncols)
    end = i.col_values(colx=1, start_rowx=1)
    print(i.row_values(rowx=0))
    print(end)
