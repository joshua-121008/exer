import numpy as np

# Create a quick test array
##my_list=[1,2,31]
##my_list=[1,2,31]
##my_list=my_list*2
##print(my_list)
##array=np.array([1,2,3,4])
##print(type(array))
#lis=np.array('')
#lis=np.array([1,2,3,4])
##lis=np.array([[1,2,3,4],[5,6,7,8]])
lis=np.array([[[1,2,3,4],[5,6,7,8]],[[0,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
dob=lis[0,0,0]+lis[0,0,1]+lis[0,0,0]+lis[1,0,0]+lis[1,0,0]+lis[2,1,3]
##print(lis[0,1,3])
print(dob)