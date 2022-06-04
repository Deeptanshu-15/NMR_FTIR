# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:01:53 2022

@author: sid
"""
import nmrglue as ng
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["figure.figsize"] = (10,10)
plt.rcParams['figure.dpi'] = 600 #inline plot dpi setting
fig,ax = plt.subplots()
dic,data = ng.bruker.read_pdata(r"C:\Users\sid\Desktop\Hydrophobization paper\NMR\11001\pdata\1") #Baseline
dic2,data2=ng.bruker.read_pdata(r"C:\Users\sid\Desktop\Hydrophobization paper\NMR\11002\pdata\1") #C6
dic3,data3=ng.bruker.read_pdata(r"C:\Users\sid\Desktop\Hydrophobization paper\NMR\11003\pdata\1") #C12
dic4,data4=ng.bruker.read_pdata(r"C:\Users\sid\Desktop\Hydrophobization paper\NMR\11004\pdata\1") #C18

data_norm = data/data.max()#normalization
data_norm2 = data2/data2.max()#normalization
data_norm3 = data3/data3.max()#normalization
data_norm4 = data4/data4.max()#normalization
udic = ng.bruker.guess_udic(dic, data_norm)
udic2 = ng.bruker.guess_udic(dic2, data_norm2)
udic3 = ng.bruker.guess_udic(dic3, data_norm3)
udic4 = ng.bruker.guess_udic(dic4, data_norm4)
# create a unit conversion object
uc = ng.fileiobase.uc_from_udic(udic)
uc2 = ng.fileiobase.uc_from_udic(udic2)
uc3 = ng.fileiobase.uc_from_udic(udic3)
uc4 = ng.fileiobase.uc_from_udic(udic4)

plt.xlabel('Chemical shift (ppm)', labelpad=20, fontsize=32)
plt.ylabel('Normalized signal intensity (a.U.)', labelpad=20, fontsize = 32)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
# plt.ylim([0,30000000])
# plt.xlim([0, 230]) #C13
plt.xlim([0, 230]) #1H
plt.ylim([0,4.5])
ax.invert_xaxis()
plt.tick_params(axis='both', pad = 10, top=True, right=True, width=1.5, size=9)
plt.minorticks_on()
plt.tick_params(which='minor',width=1, size=6)
# ax.plot(udic.ppm_scale(), data_norm)
ppm_scale = uc.ppm_scale()
ppm_scale2 = uc2.ppm_scale()
ppm_scale3 = uc3.ppm_scale()
ppm_scale4 = uc4.ppm_scale()
plt.plot(ppm_scale4, data_norm4+3, color = "#A52A2A", label = "$\mathregular {C_{18}}$")
plt.plot(ppm_scale3, data_norm3+2, color = "#FF0000", label = "$\mathregular {C_{12}}$")
plt.plot(ppm_scale2, data_norm2+1, color = "#FFA500", label = "$\mathregular {C_{6}}$")
plt.plot(ppm_scale, data_norm, color = "#696969", label = "Baseline")
plt.tick_params(axis='both', pad = 10, top=True, right=True)
plt.grid(which='major', color='#DDDDDD', linewidth=1.25)
plt.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=1.0)
plt.minorticks_on()
plt.legend(fontsize=22, frameon=False, loc='best')
# plt.scatter(peak_locations_ppm, peak_amplitudes, s=300)
