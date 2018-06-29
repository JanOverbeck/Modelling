# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:06:07 2017

@author: ovj
"""

import numpy as np
import matplotlib.pyplot as plt
import RamanFittingFunctions as RamFit #current WD correctly set? os.getcwd()
import scipy.constants as cst
import math

lambda0=532
lambda1=544
lambda2=556
lambda3=568
lambda4=580


n=20
listn=np.arange(15,45,1,int)
listnje=np.arange(1.7,1.95,0.01,float)
nje=1.83
d=3500
listd=np.arange(2500,5000,100,int)

ListDelTot=[]
ArrDelTot=np.zeros([len(listn)*len(listnje)*len(listd),4])


i=0
for idx2,d in enumerate(listd):
    for idx1,nje in enumerate(listnje):
        for idx, n in enumerate(listn): 
            Deld1=(n+1)*lambda1/(2*nje)-d
            Deld2=(n+2)*lambda2/(2*nje)-d
            Deld3=(n+3)*lambda3/(2*nje)-d
            Deld4=(n+4)*lambda4/(2*nje)-d
    #        DelTot = abs(Deld1)+abs(Deld2)+abs(Deld3)+abs(Deld4)
            DelTot = Deld1**2+Deld2**2+Deld3**2+Deld4**2
            ArrDelTot[i,0]=n
            ArrDelTot[i,1]=DelTot
            ArrDelTot[i,2]=nje
            ArrDelTot[i,3]=d
            i+=1
    

print(ArrDelTot[np.where(ArrDelTot == min(ArrDelTot[:,1]))[0][0]])

