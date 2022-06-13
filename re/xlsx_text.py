import xlrd

book = xlrd.open_workbook("income.xls")

# 得到所有sheet对象
sheets = book.sheets()

incomeOf3years = 0
for sheet in sheets:
    # 收入在第2列
    incomes = sheet.col_values(colx=1, start_rowx=1)
    # 去掉包含星号的月份收入
    toSubstract = 0
    # 月份在第1列
    monthes = sheet.col_values(colx=0)

    for row, month in enumerate(monthes):
        if type(month) is str and month.endswith('*'):
            income = sheet.cell_value(row, 1)
            print(month, income)
            toSubstract += income

    actualIncome = int(sum(incomes) - toSubstract)
    print(f"{sheet.name}年真实收入为: {actualIncome}")
    incomeOf3years += actualIncome

print(f'全部收入为{incomeOf3years}')
