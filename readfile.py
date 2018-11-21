# Reading an excel file using Python 

import shutil
import xlrd 
import os
import sys

# Give the location of the file 
loc = ("Readfile_.xlsx") 

# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

# For row 0 and column 0 
#sheet.cell_value(0, 0) 
#print sheet.cell_value(0,0)
#print sheet.cell_value(0,1)
print (sheet.nrows)
print (sheet.ncols)

for i in range(sheet.nrows):
	path=sheet.cell_value(i,1)
	print path
	filename=sheet.cell_value(i,0)
	print filename
	#print "path"+path
	
	if not os.path.exists(path):
		os.makedirs(path)
	shutil.move(filename,path)
		

	
	