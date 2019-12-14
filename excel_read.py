import xlrd


def pas_lst():
    # file name
    # xlrd file should be in same file
    workbook = xlrd.open_workbook("test.xlsx")
    # name of the name of sheet by index

    worksheet = workbook.sheet_by_index(0)
    total_row = worksheet.nrows
    total_col = worksheet.ncols

    l = []
    for i in range(total_row):
        if worksheet.cell(i, 2).value == '':
            l.append((worksheet.cell(i, 0).value, worksheet.cell(i, 1).value))
        else:
            l.append((worksheet.cell(i, 0).value, worksheet.cell(i, 1).value, worksheet.cell(i, 2).value))

    return (l)


if __name__ == '__main__':
    print(pas_lst())
