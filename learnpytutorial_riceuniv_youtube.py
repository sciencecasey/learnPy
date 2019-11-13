import numpy as np

#create 1 dimensional arrays (vectors)
my_array = np.array([0,1,2,3])
my_array
my_array.dtype #see what type of array it is saved as (integer)
str_array=my_array.astype(str)
str_array #make a string array

#see the difference in how string or integer arrays are treated
for i in my_array:
    print(i*4)

for i in str_array:
    print(i*4)

#create a 2-dimensional array with rows and columns
dim2_array=np.array([[0,1,2,3],[0,1,2,3],[0,1,2,4]])
#each nested bracket is a row
dim2_array.ndim #see if 1,2,3 dimensional
dim2_array.shape #see the shape (rows,columns)
dim2_array.size #see the number of items total

#mean of all the items
np.mean(dim2_array)

#means of column by column or row by row
#axis=0 represents the average of each column
np.mean(dim2_array, axis = 0)
#axis=1 represents rows
np.mean(dim2_array, axis=1)

#index an array
dim2_array[0] # indexes at the topmost row
dim2_array[3] #index at the bottommost rows
dim2_array[:]#index all rows and columns
dim2_array[:2] #index the 0-2 rows
dim2_array[:2,:] #index 0-2 rows, all columns
dim2_array[:,:3] #indexes 0-3 columns
dim2_array[:2,3:4] #indexes the 2nd row at column 4 (from 3-4 is 4)

#reverse order
dim2_array[2][::-1] #index row 3 and reverse it's order
dim2_array[::-1] #reverse the order of the rows
dim2_array[:,::-1] #reverse the order of the columns

#save item as a csv
#first must specify location
import os
datadir=os.path.expanduser('/Users/CaseyJayne/Desktop/working_folder/insightsecurtiy/data/')
np.savetxt(os.path.join(datadir, 'derivatives', 'viewingarray.csv'), dim2_array, delimiter=',')
#np.savetxt('viewingarray.csv', dim2_array, delimiter = ',')

#np.save 'tab' tells you the options for endings

np.genfromtxt(os.path.join(datadir, 'derivatives', 'viewingarray.csv'), delimiter=',')
