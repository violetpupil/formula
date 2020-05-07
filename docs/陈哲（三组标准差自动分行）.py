#!usr/bin/env python
#encoding:utf-8
EA=[426.78,419.76,419.94]
n=[2.58,3.12,4.39]
w=0.5
b=[1,2,3]
#计算a
print ('b=')
from itertools import product
num_list=b
num=len(num_list)
res_list=list(product(num_list,repeat=num))
for v in res_list:
    print(v)
print ('-------------------------------------')
#print(res_list[0])
print ('a=')
i=0
j=0
A = [[0] * len(num_list) for _ in range(len(res_list))]
while i<len(res_list):
    while j<len(num_list):
        A[i][j]=n[j]-w*res_list[i][j]
        A[i][j]=round(A[i][j],4)
        j=j+1
    print(A[i])
    i=i+1
    j=0
#print(A)
print ('-------------------------------------')
#计算EN,EG
print('EN=x,EG=y')
from sympy import*
from sympy.abc import x,y
import math
A1 = [[0] * (len(num_list)+1) for _ in range(len(res_list))]
B1 = [[0] * (len(num_list)+1) for _ in range(len(res_list))]
EA1= [0 for i in range(len(num_list)+1)]
i=0
j=0
while i<len(res_list):
    while j<len(num_list):
        A1[i][j]=A[i][j]
        B1[i][j]=res_list[i][j]
        EA1[j]=EA[j]
        j=j+1
    i=i+1
    j=0
i=0
j=0
while i<len(res_list):
    A1[i][3]=A[i][0]
    B1[i][3]=res_list[i][0]
    EA1[3]=EA[0]
    i=i+1
aa=[[0] * (len(num_list)+4) for _ in range(len(res_list))]
i=0
j=0
while i<len(res_list):
    while j<len(num_list):
        a=A1[i][j]
        b=B1[i][j]
        aa[i][j]= solve([A1[i][j]*x+B1[i][j]*w*y-EA1[j]*(A1[i][j]+B1[i][j]*w),A1[i][j+1]*x+B1[i][j+1]*w*y-EA1[j+1]*(A1[i][j+1]+B1[i][j+1]*w)],[x,y])
        aa[i][j][x]=round(aa[i][j][x],2)
        aa[i][j][y]=round(aa[i][j][y],2)
        j=j+1
    aa[i][j]=round((aa[i][0][x]+aa[i][1][x]+aa[i][2][x])/3,2)
    aa[i][j+1]=round(math.sqrt((aa[i][0][x]-aa[i][j])**2+(aa[i][1][x]-aa[i][j])**2+(aa[i][2][x]-aa[i][j])**2),2)
    aa[i][j+2]=round((aa[i][0][y]+aa[i][1][y]+aa[i][2][y])/3,2)
    aa[i][j+3]=round(math.sqrt((aa[i][0][y]-aa[i][j+2])**2+(aa[i][1][y]-aa[i][j+2])**2+(aa[i][2][y]-aa[i][j+2])**2),2)
    print(aa[i])
    i=i+1
    j=0
#print('EN=x,EG=y\n',aa)

