#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:03:50 2018

@author: carltonx
"""
#### temp depencence on HOM and MCM compounds
## edited for NOx dependence as well

import numpy as np
from netCDF4 import * 
from ncread import nc_read
import matplotlib.pyplot as plt
import pandas as pd


#path       = '/home/local/carltonx/Work/Malte_box/Project_runs/netcdf_input/'
path_vap   = '/home/carltonx/Work/Malte_box/Project_runs/old_malte_in/Malte_in/Box/Test1234/new_chem/'
path       = '/media/carltonx/Seagate Expansion Drive/netcdf_output/Temp_and_nox_data_sep/' 

vap_prop = np.loadtxt(path_vap+'Vapour_properties.dat')
vap_name = genfromtxt(path_vap+'Vapour_names.dat',dtype='str')
vap_oc   = loadtxt(path_vap+'Vapour_O_C_ratio_Carlton.dat')

## Temperature data
f_258_4   = Dataset(path+'apin258_4.nc','r')
f_258_100 = Dataset(path+'apin258_100.nc','r')


f_278_4   = Dataset(path+'apin278_4.nc','r')
f_278_100 = Dataset(path+'apin278_100.nc','r')


f_293_4   = Dataset(path+'apin293_4.nc','r')
f_293_100 = Dataset(path+'apin293_100.nc','r')


f_303_4   = Dataset(path+'apin303_4.nc','r')
f_303_100 = Dataset(path+'apin303_100.nc','r')


f_313_4   = Dataset(path+'apin313_4.nc','r')
f_313_100 = Dataset(path+'apin313_100.nc','r')

## NOx data

f_125_4   = Dataset(path+'apin125_4.nc','r')
f_125_100 = Dataset(path+'apin125_100.nc','r')


f_250_4   = Dataset(path+'apin250_4.nc','r')
f_250_100 = Dataset(path+'apin250_100.nc','r')

#########
## Temperature

c258_4,v258_4,es258_4,n258_4           = nc_read(f_258_4)                            ## 4 ppb O3   
c258_100,v258_100,es258_100,n258_100   = nc_read(f_258_100)                          ## 100 ppb O3

c278_4,v278_4,es278_4,n278_4           = nc_read(f_278_4)
c278_100,v278_100,es278_100,n278_100   = nc_read(f_278_100)

c293_4,v293_4,es293_4,n293_4           = nc_read(f_293_4)
c293_100,v293_100,es293_100,n293_100   = nc_read(f_293_100)

c303_4,v303_4,es303_4,n303_4           = nc_read(f_303_4)
c303_100,v303_100,es303_100,n303_100   = nc_read(f_303_100)

c313_4,v313_4,es313_,n313_4            = nc_read(f_313_4)
c313_100,v313_100,es313_100,n313_100   = nc_read(f_313_100)


# NOx data read
c125_4,v125_4,es125_4,n125_4           = nc_read(f_125_4)                            ## 4 ppb O3   
c125_100,v125_100,es125_100,n125_100   = nc_read(f_125_100)                          ## 100 ppb O3

c250_4,v250_4,es250_4,n250_4           = nc_read(f_250_4)
c250_100,v250_100,es250_100,n250_100   = nc_read(f_250_100)


 # indices for all compounds 
hom_ind       = [i for i, s in enumerate(vap_name[:-1]) if 'HOM' in s]
mcm_ind       = [i for i, s in enumerate(vap_name[:-1]) if 'HOM' not in s]

## temeprature
## 258
hom_abs_258_4       = sum(c258_4[hom_ind])                                           # contribution by all HOM compounds in ug/m3
mcm_abs_258_4       = sum(c258_4[mcm_ind])                                           # contribution by all MCM compounds in ug/m3

hom_abs_258_100     = sum(c258_100[hom_ind])                                         # contribution by all HOM compounds in ug/m3
mcm_abs_258_100     = sum(c258_100[mcm_ind])                                         # contribution by all MCM compounds in ug/m3

## 278
hom_abs_278_4       = sum(c278_4[hom_ind])                                           # contribution by all HOM compounds in ug/m3
mcm_abs_278_4       = sum(c278_4[mcm_ind])                                           # contribution by all MCM compounds in ug/m3

hom_abs_278_100     = sum(c278_100[hom_ind])                                         # contribution by all HOM compounds in ug/m3
mcm_abs_278_100     = sum(c278_100[mcm_ind])                                         # contribution by all MCM compounds in ug/m3

## 293
hom_abs_293_4       = sum(c293_4[hom_ind])                                           # contribution by all HOM compounds in ug/m3
mcm_abs_293_4       = sum(c293_4[mcm_ind])                                           # contribution by all MCM compounds in ug/m3

hom_abs_293_100     = sum(c293_100[hom_ind])                                         # contribution by all HOM compounds in ug/m3
mcm_abs_293_100     = sum(c293_100[mcm_ind])                                         # contribution by all MCM compounds in ug/m3

## 303
hom_abs_303_4       = sum(c303_4[hom_ind])                                           # contribution by all HOM compounds in ug/m3
mcm_abs_303_4       = sum(c303_4[mcm_ind])                                           # contribution by all MCM compounds in ug/m3

hom_abs_303_100     = sum(c303_100[hom_ind])                                         # contribution by all HOM compounds in ug/m3
mcm_abs_303_100     = sum(c303_100[mcm_ind])                                         # contribution by all MCM compounds in ug/m3

## 313
hom_abs_313_4       = sum(c313_4[hom_ind])                                           # contribution by all HOM compounds in ug/m3
mcm_abs_313_4       = sum(c313_4[mcm_ind])                                           # contribution by all MCM compounds in ug/m3

hom_abs_313_100     = sum(c313_100[hom_ind])                                         # contribution by all HOM compounds in ug/m3
mcm_abs_313_100     = sum(c313_100[mcm_ind])                                         # contribution by all MCM compounds in ug/m3

## NOx data

hom_abs_125_4       = sum(c125_4[hom_ind])                                           # contribution by all HOM compounds in ug/m3
mcm_abs_125_4       = sum(c125_4[mcm_ind])                                           # contribution by all MCM compounds in ug/m3

hom_abs_125_100     = sum(c125_100[hom_ind])                                         # contribution by all HOM compounds in ug/m3
mcm_abs_125_100     = sum(c125_100[mcm_ind])                                         # contribution by all MCM compounds in ug/m3

hom_abs_250_4       = sum(c250_4[hom_ind])                                           # contribution by all HOM compounds in ug/m3
mcm_abs_250_4       = sum(c250_4[mcm_ind])                                           # contribution by all MCM compounds in ug/m3

hom_abs_250_100     = sum(c250_100[hom_ind])                                         # contribution by all HOM compounds in ug/m3
mcm_abs_250_100     = sum(c250_100[mcm_ind])                                         # contribution by all MCM compounds in ug/m3

## creating arrays for temperature data
hom_100 = np.array([hom_abs_258_100, hom_abs_278_100, hom_abs_293_100, hom_abs_303_100, hom_abs_313_100])
hom_4   = np.array([hom_abs_258_4, hom_abs_278_4, hom_abs_293_4, hom_abs_303_4, hom_abs_313_4])

mcm_100 = np.array([mcm_abs_258_100, mcm_abs_278_100, mcm_abs_293_100, mcm_abs_303_100, mcm_abs_313_100])
mcm_4   = np.array([mcm_abs_258_4, mcm_abs_278_4, mcm_abs_293_4, mcm_abs_303_4, mcm_abs_313_4])

## NOx data
hom_no_100 = np.array([hom_abs_293_100, hom_abs_125_100, hom_abs_250_100]) ##2.5, 12.5, 25
hom_no_4   = np.array([hom_abs_293_4, hom_abs_125_4, hom_abs_250_4])

mcm_no_100 = np.array([mcm_abs_293_100, mcm_abs_125_100, mcm_abs_250_100])
mcm_no_4   = np.array([mcm_abs_293_4, mcm_abs_125_4, mcm_abs_250_4])

### figure for temperature

fig = plt.figure(num=None, figsize=(18, 12), dpi=120, facecolor='w', edgecolor='k')
barwidth = 0.8
tickpos  = [2,7,12,17,22] 
 ## X position of bars
r1 = [1,6,11,16,21]
r2 = [2,7,12,17,22]
r3 = [3,8,13,18,23]
r4 = [4,9,14,19,24]


## bar plots
plt.bar(r1,hom_4, width = barwidth, color=(0.3,0.1,0.4,0.6), label='Total PRAM contribution at 4ppb $O_3$')
plt.bar(r2,hom_100, width = barwidth, color='orange', label='Total PRAM contribution at 100 ppb $O_3$')
plt.bar(r3,mcm_4, width = barwidth, color=(0.3,0.9,0.4,0.6), label='Total MCM contribution at 4ppb $O_3$')
plt.bar(r4,mcm_100, width = barwidth, color='grey', label='Total MCM contribution at 100 ppb $O_3$ ') 


plt.legend(fontsize=16, loc='upper right' )
plt.ylim(top = 150)

plt.xlabel('Temperature (K)', fontsize=20)
plt.ylabel(r'SOA mass loadings $(\mu$g/$m^3$)', fontsize = 20)
plt.xticks(tickpos,['258.15 K','278.15 K','293.15 K','303.15 K','313.15 K'],fontsize=16)
plt.yticks(fontsize = 16)
plt.title(r'$\alpha$-pinene (50 ppb) - $O_3$ - Temperature dependence', fontsize = 18)
plt.savefig('/home/local/carltonx/Work/Paper 1/plots_py/temp_bar.png',bbox_inches = 'tight')

 
 ### figure for nox
 
fig = plt.figure(num=None, figsize=(18, 12), dpi=120, facecolor='w', edgecolor='k')
barwidth = 0.8
tickpos  = [2,7,12] 
 
## X position of bars
n1 = [1,6,11]
n2 = [2,7,12]
n3 = [3,8,13]
n4 = [4,9,14]

## bar plots
plt.bar(n1,hom_no_4, width = barwidth, color=(0.3,0.1,0.4,0.6), label='Total PRAM contribution at 4ppb $O_3$')
plt.bar(n2,hom_no_100, width = barwidth, color='orange', label='Total PRAM contribution at 100 ppb $O_3$')
plt.bar(n3,mcm_no_4, width = barwidth, color=(0.3,0.9,0.4,0.6), label='Total MCM contribution at 4ppb $O_3$')
plt.bar(n4,mcm_no_100, width = barwidth, color='grey', label='Total MCM contribution at 100 ppb $O_3$') 


plt.legend(fontsize=16, loc='upper right' )
plt.ylim(top = 50)

plt.xlabel('$NO_x$ (ppb)', fontsize=20)
plt.ylabel(r'SOA mass loadings $(\mu$g/$m^3$)', fontsize = 20)
plt.yticks(fontsize = 16)
plt.xticks(tickpos,['2.5 ppb','12.5 ppb','25.0 ppb'],fontsize=16)
plt.title(r'$\alpha$-pinene (50 ppb) - $O_3$ - $NO_x$ dependence', fontsize = 18)
plt.savefig('/home/local/carltonx/Work/Paper 1/plots_py/nox_bar.png',bbox_inches = 'tight')



