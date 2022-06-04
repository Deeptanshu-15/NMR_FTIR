# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 09:44:00 2022

@author: sid
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import spectrochempy as spc
from scipy.signal import find_peaks
import os
# f=[]
# mypath=r'C:\Users\sid\Desktop\Hydrophobization paper\FTIR'
# for (dirpath, dirnames, filenames) in os.walk(mypath):
#     f.extend(filenames) #Stores filenames into a list
#     break
# book = {} #dictionary array
# print(f)

# Pr = input("\n Input the dataset to print: ") #raw_input for input of digits and characters
# Pr_print = str(Pr) + ' % P750 Compression Test'
    
plt.rcParams['figure.dpi'] = 600 #inline plot dpi setting
plt.rcParams["figure.figsize"] = (10,10)
fig, ax = plt.subplots()
book = pd.read_csv(r"C:\Users\sid\Desktop\Hydrophobization paper\FTIR\CNF100-DeepuYael_210215.0")
book2 = pd.read_csv(r"C:\Users\sid\Desktop\Hydrophobization paper\FTIR\Exp44_C6.0")
book3 = pd.read_csv(r"C:\Users\sid\Desktop\Hydrophobization paper\FTIR\Exp46_C12.0")
book4 = pd.read_csv(r"C:\Users\sid\Desktop\Hydrophobization paper\FTIR\Exp45_C18.0")
book5 = pd.read_csv(r"C:\Users\sid\Desktop\Hydrophobization paper\FTIR\c12.0")
book6 = pd.read_csv(r"C:\Users\sid\Desktop\Hydrophobization paper\FTIR\C18.0")
book.columns = ["Wavenumber", "Intensity"]
book2.columns = ["Wavenumber", "Intensity"]
book3.columns = ["Wavenumber", "Intensity"]
book4.columns = ["Wavenumber", "Intensity"]
book5.columns = ["Wavenumber", "Intensity"]
book6.columns = ["Wavenumber", "Intensity"]
bi = book.Intensity/book.Intensity.max()
bi2 = book2.Intensity/book2.Intensity.max()
bi3 = book3.Intensity/book3.Intensity.max()
bi4 = book4.Intensity/book4.Intensity.max()
bi5 = book5.Intensity/book5.Intensity.max()
bi6 = book6.Intensity/book6.Intensity.max()

peaks, properties = find_peaks(bi, prominence=0.001)  #index of peak
peaks2, properties2 = find_peaks(bi2, prominence=0.001)
peaks3, properties3 = find_peaks(bi3, prominence=0.001)
peaks4, properties4 = find_peaks(bi4, prominence=0.001)

peaks_int = np.zeros(len(peaks))
peaks_int2 = np.zeros(len(peaks2))
peaks_int3 = np.zeros(len(peaks3))
peaks_int4 = np.zeros(len(peaks4))
for i in range(len(peaks)):
    peaks_int[i] = book.Intensity[peaks[i]]
for i in range(len(peaks2)):
    peaks_int2[i] = book2.Intensity[peaks2[i]]
for i in range(len(peaks3)):
    peaks_int3[i] = book3.Intensity[peaks3[i]]
for i in range(len(peaks2)):
    peaks_int4[i] = book4.Intensity[peaks4[i]]
#Graphing
ax.set_facecolor(color='white')
plt.plot(book4.Wavenumber,bi4+2.25, label = '$\mathregular {C_{18}}$', color = '#A52A2A', linewidth=1.5)
# plt.plot(book6.Wavenumber,bi6+2.25, label = 'Stearoyl chloride $\mathregular {C_{18}}$', color = '#A52A2A', ls='--', linewidth=1.5)
plt.plot(book3.Wavenumber,bi3+1.5, label = '$\mathregular {C_{12}}$', color = '#FF0000', linewidth=1.5)
# plt.plot(book5.Wavenumber,bi5+1.5, label = 'Lauroyl chloride $\mathregular {C_{12}}$', color = '#FF0000', ls='--', linewidth=1.5)
plt.plot(book2.Wavenumber,bi2+0.75, label = '$\mathregular {C_{6}}$', color = '#FFA500', linewidth=1.5)
# plt.plot(book5.Wavenumber,(book5.Intensity*5)+0.75, label = 'Hexanoyl Chloride $\mathregular {C_{6}}$', color = '#FFA500', ls='--', linewidth=1.5)
plt.plot(book.Wavenumber,bi, label = 'Baseline', color = '#696969', linewidth=1.5)
# plt.scatter(book.Wavenumber[peaks], bi[peaks], s=120, marker ='x', color = '#696969')
# plt.scatter(book2.Wavenumber[peaks2], bi2[peaks2]+0.75, s=120, marker ='x', color = '#FFA500')
# plt.scatter(book3.Wavenumber[peaks3], bi3[peaks3]+1.5, s=120, marker ='x', color = '#FF0000')
# plt.scatter(book4.Wavenumber[peaks4], bi4[peaks4]+2.25, s=120, marker ='x', color = '#A52A2A')
# plt.vlines(x=book.Wavenumber[peaks], ymin=0,
#             ymax = book.Intensity[peaks], color = "C1")
plt.xlabel('Wavernumber ($\mathregular {nm^{-1}}$)', labelpad=20, fontsize=32)
plt.legend(fontsize=20, frameon=False, loc='best')
plt.ylabel('Normalized absorbance (a.U.)', labelpad=20, fontsize = 32)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
# plt.figtext(.7, .7, fontsize = 24)
plt.xlim([400,4000])
# plt.ylim([0,0.7])
plt.ylim([0,3.5])
plt.tick_params(axis='both', pad = 10, top=True, right=True)
plt.grid(which='major', color='#DDDDDD', linewidth=1.25)
plt.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=1.0)
plt.minorticks_on()
for axis in ['top', 'bottom', 'left','right']:
    ax.spines[axis].set_linewidth(2.0)
plt.show()