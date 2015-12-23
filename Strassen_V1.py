'create matrixes'
import random
import numpy as np
def generateMatrix_A(m, n):
    A = list([])
    for i in range(m):
        row = list()
        for j in range(n):
            row.append(random.randint(0, 1000))
        A.append(row)
    return A
 
def generateMatrix_B(l, k):
    B = list([])
    for i in range(k):
        row = list()
        for j in range(l):
            row.append(random.randint(0, 1000))
        B.append(row)
    return B

from itertools import starmap, zip_longest
from operator import add
 

n = random.randint(2, 6)
x = 2**n
 
A = generateMatrix_A(x, x)
print('Matrix A:')
print(A)
 
B = generateMatrix_B(x, x)
print('Matrix  B:')
print(B)

'matrix summing'
def ad(m1,m2):
    t=[]   #временная матрица
    z=[]   #конечная матрица
    s=0
    r1=len(m1) #количество строк в первой матрице #Количество столбцов в 1   
             #и строк во 2ой матрице # количество столбцов во 2ой матрице
    for i in range(0,r1):
        for j in range(0,r1):
            s=m1[i][j]+m2[i][j]
            t.append(s)
            s=0
        z.append(t)
        t=[]           
    return z

'matrix difference'
def di(m1,m2):
    t=[]   #временная матрица
    z=[]   #конечная матрица
    s=0
    r1=len(m1) #количество строк в первой матрице #Количество столбцов в 1   
             #и строк во 2ой матрице # количество столбцов во 2ой матрице
    for i in range(0,r1):
        for j in range(0,r1):
            s=m1[i][j]-m2[i][j]
            t.append(s)
            s=0
        z.append(t)
        t=[]           
    return z
        

    
'matrix multiplying'
def matrixmult(m1,m2):
    s=0     #
    t=[]    #временная матрица
    m3=[]   #конечная матрица
         
    r1=len(m1) #количество строк в первой матрице
    c1=len(m1[0]) #Количество столбцов в 1   
    r2=c1           #и строк во 2ой матрице
    c2=len(m2[0])  # количество столбцов во 2ой матрице
    for z in range(0,r1):
        for j in range(0,c2):
            for i in range(0,c1):
                s=s+m1[z][i]*m2[i][j]
            t.append(s)
            s=0
        m3.append(t)
        t=[]           
    return m3

'дробилка матриц'
def M11(a):
    t=[]   #временная матрица
    a11=[]   #lefthight corner
    s=0
    v=int(x/2)
    
    for i in range(0,v):
        for j in range(0,v):
            s=a[i][j]
            t.append(s)
            s=0
        a11.append(t)
        t=[]           
    return a11

def M12(a):
    t=[]   #временная матрица
    a12=[]   #lefthight corner
    s=0
    v=int(x/2)
    
    for i in range(0,v):
        for j in range(v,x):
            s=a[i][j]
            t.append(s)
            s=0
        a12.append(t)
        t=[]           
    return a12

def M21(a):
    t=[]   #временная матрица
    a21=[]   #lefthight corner
    s=0
    v=int(x/2)
    
    for i in range(v,x):
        for j in range(0,v):
            s=a[i][j]
            t.append(s)
            s=0
        a21.append(t)
        t=[]           
    return a21

def M22(a):
    t=[]   #временная матрица
    a22=[]   #lefthight corner
    s=0
    v=int(x/2)
    
    for i in range(v,x):
        for j in range(v,x):
            s=a[i][j]
            t.append(s)
            s=0
        a22.append(t)
        t=[]           
    return a22

a11 = M11(A)
a12 = M12(A)
a21 = M21(A)
a22 = M22(A)
b11 = M11(B)
b12 = M12(B)
b21 = M21(B)
b22 = M22(B)




P1 = matrixmult(ad(a11, a22), ad(b11, b22))
P2 = matrixmult(ad(a21, a22), b11)
P3 = matrixmult(a11, di(b12, b22))
P4 = matrixmult(a22, di(b21, b11))
P5 = matrixmult(ad(a11, a12), b22)
P6 = matrixmult(di(a21, a11), ad(b11, b12))
P7 = matrixmult(di(a12, a22), ad(b21, b22))

C11 = ad(di(ad(P1, P4), P5), P7)
C12 = ad(P3, P5)
C21 = ad(P2, P4)
C22 = ad(ad(di(P1, P2),P3),P6)


print('C11')
print('C12')
print('C21')
print('C22')

print(C11)
print(C12)
print(C21)
print(C22)


CH = C11+C21
CL = C12+C22

print('chcl')
print(CH)
print(CL)
