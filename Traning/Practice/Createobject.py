'''
def username():
    name = input("Enter your name: ")
    print(name[-1])
username()

def last_char(name):
    return name[-1]
print(last_char("shivam"))



import xlrd

pt = (r"C:\\Users\\admin\\Downloads\\Upload_file\\Attendance_Report_hardware_team_monthly.xls")
wb=xlrd.open_workbook(pt)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)'''