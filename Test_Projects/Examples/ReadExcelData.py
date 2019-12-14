import xlrd


path = "C:\\Users\\admin\\Documents\\Activation_hits.xlsx"


book = xlrd.open_workbook(path)

print(book.nsheets)
print(book.sheet_names())

firstworksheet = book.sheet_by_index(0)

firstworksheet.row_values(0)
firstcol = firstworksheet.col_values(0)
lenCol = len(firstcol)

colname = []

for i in range(lenCol):
    colname.append(firstcol[i])
print(colname)

string =  [1,2,3,4,5]
lenstr = len(string)
num=[]
for i in range(lenstr):
    num.append(string[i])
    print(num)