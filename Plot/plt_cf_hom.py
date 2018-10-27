#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 12:55:10 2018

@author: carltonx
"""

from numpy import *
import matplotlib.pyplot as plt
 
path_hom      = '/home/local/carltonx/Work/Malte_box/Project_runs/sep_update_res/Hom_normal/'
path_cf_hom   = '/home/local/carltonx/Work/Malte_box/Project_runs/sep_update_res/CF_hom/'

f1  = loadtxt(path_hom+'apinene.dat')
f2  = loadtxt(path_cf_hom+'apinene_cf_hom.dat')

mw1 = 136.23

# apinene
C_oa_f1 = f1[:,5]/100 * (f1[:,4] * mw1 * 12.187 / 293.15) #ug/m3 mass concetration of organic aerosol in condensed phase
dcoa_f1 = f1[:,4] * mw1  * 12.187 / 293.15 # ug/m3 reacted voc
amf_f1  = C_oa_f1 / dcoa_f1 # yield

# bpinene
C_oa_f2 = f2[:,5]/100 * (f2[:,4] * mw1 * 12.187 / 293.15)
dcoa_f2 = f2[:,4] * mw1  * 12.187 / 293.15
amf_f2  = C_oa_f2 / dcoa_f2


### figure

plt.figure(num=None, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')

plt.scatter(C_oa_f1[np.where(f1[:,2] != 0)],amf_f1[np.where(f1[:,2] != 0)], 50,
              c='r',marker='o',label='Batch mode')
plt.scatter(C_oa_f2[np.where(f2[:,2] != 0)],amf_f2[np.where(f2[:,2] != 0)], 50,
             c='b',marker='s',label='Continuous flow')

plt.legend(loc='upper left',fontsize=16)

plt.xlabel(r'SOA mass loadings$(\mu$g/$m^3$)',fontsize=20)
plt.xticks(fontsize=14, rotation=0)
plt.ylabel('Mass yields',fontsize=20)
plt.yticks(fontsize=14, rotation=0)
plt.xscale('log')
plt.grid(True)
plt.title(r'$\alpha$-pinene - $O_{3}$')