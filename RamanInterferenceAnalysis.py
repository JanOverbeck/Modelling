# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:48:01 2017

@author: ovj

%reset does magic


"""

import numpy as np
import matplotlib.pyplot as plt
import RamanFittingFunctions as RamFit #current WD correctly set? os.getcwd()
import scipy.constants as cst
import math

h = np.arange(0,1001,1)
WLin = [488,532,785]
Plotting =["b-","g-","r-"]
nALD = 1.650 # Corina Barbos, Danièle Blanc-Pelissier, Alain Fave & Elisabeth Blanquet et al. Characterization of Al2O3 Thin Films Prepared by Thermal ALD.
nAIR = 1.0
step = np.zeros((1,1001))
step[0,580:680]=1


IG = np.sin(4*math.pi*h/RamFit.relcm2nm(532,1685))+1.1
I2D = np.sin(4*math.pi*h/RamFit.relcm2nm(532,2670))+1.1

RamFit.relcm2nm(514.5,1586)           
Ephoton = 10**9*(cst.h*cst.c)/(cst.e*1240) # energy in eV
RamFit.nm2Ephoton(1240)


fig1 = plt.figure("input")     # a new figure window       
ax1 = fig1.add_subplot(111)# ax1 is an Axes element ("plotting Window"). Specify (nrows, ncols, axnum)
ax1.set_title("input intensities")
ax1.set_xlabel("height [nm]")
ax1.set_ylabel("intensity [arb.u.]")
ax1.plot(h,IG)
ax1.plot(h,I2D)
fig1.show()

fig2 = plt.figure("relInt")     # a new figure window       
ax2 = fig2.add_subplot(111)# ax1 is an Axes element ("plotting Window"). Specify (nrows, ncols, axnum)
ax2.set_title("I2D/IG")
ax2.set_xlabel("height [nm]")
ax2.set_ylabel("I2D/IG [arb.u.]")
ax2.plot(h,I2D/IG)
fig2.show()



fig3 = plt.figure("Iin")     # a new figure window       
ax3 = fig3.add_subplot(111)# ax1 is an Axes element ("plotting Window"). Specify (nrows, ncols, axnum)
ax3.set_title("I_incident vs. h - ALD")
ax3.set_xlabel("height [nm]")
ax3.set_ylabel("I_incident [arb.u.]")

for WL in WLin:
    Iin = np.sin(2*math.pi*h/WL*nALD)**2
    ax3.plot(h,Iin)

ax3.plot(h,step[0][:])
fig3.show()


fig4 = plt.figure("Iin")     # a new figure window       
ax4 = fig4.add_subplot(111)# ax1 is an Axes element ("plotting Window"). Specify (nrows, ncols, axnum)
ax4.set_title("I_incident vs. h - Air/Vac")
ax4.set_xlabel("height [nm]")
ax4.set_ylabel("I_incident [arb.u.]")

for i,WL in enumerate(WLin):   
    
    Iin = np.sin(2*math.pi*h/WL*nAIR)**2
    ax4.plot(h,Iin,Plotting[i])

ax4.plot(h,step[0][:],'k-')
fig4.show()