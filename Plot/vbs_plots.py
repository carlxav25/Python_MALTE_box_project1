#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:46:17 2018

@author: carltonx
"""

## vbs plots


from numpy import *
from ncread import nc_read
from netCDF4 import *
import matplotlib.pyplot as plt


path       = '/home/local/carltonx/Work/Malte_box/Project_runs/netcdf_input/'
path_vap   = '/home/local/carltonx/Work/Malte_box/Project_runs/malte_box/Malte_in/Box/Test1234/new_chem/'

vap_prop = loadtxt(path_vap+'Vapour_properties.dat')
vap_name = genfromtxt(path_vap+'Vapour_names.dat',dtype='str')
vap_oc   = loadtxt(path_vap+'Vapour_O_C_ratio_Carlton.dat')



def io_vbs(cond, vap, eff_sat):
 
 ## index   
 ind_l65 = where((eff_sat > 1e-6) & (eff_sat <= 1e-5))
 ind_l54 = where((eff_sat > 1e-5) & (eff_sat <= 1e-4)) 
 ind_l43 = where((eff_sat > 1e-4) & (eff_sat <= 1e-3))  
 ind_l32 = where((eff_sat > 1e-3) & (eff_sat <= 1e-2))   
 ind_l21 = where((eff_sat > 1e-2) & (eff_sat <= 1e-1))
 ind_l10 = where((eff_sat > 1e-1) & (eff_sat <= 1)) 
 ind_l01 = where((eff_sat > 1) & (eff_sat <= 10))  
 ind_l12 = where((eff_sat > 10) & (eff_sat <= 1e2))
 ind_l23 = where((eff_sat > 1e2) & (eff_sat <= 1e3))   
 
 ## condensed phase
 c65     = sum(cond[ind_l65])
 c54     = sum(cond[ind_l54])
 c43     = sum(cond[ind_l43])
 c32     = sum(cond[ind_l32])
 c21     = sum(cond[ind_l21])
 c10     = sum(cond[ind_l10])
 c01     = sum(cond[ind_l01])
 c12     = sum(cond[ind_l12])
 c23     = sum(cond[ind_l23])
 
 ## condensed phase
 v65     = sum(vap[ind_l65])
 v54     = sum(vap[ind_l54])
 v43     = sum(vap[ind_l43])
 v32     = sum(vap[ind_l32])
 v21     = sum(vap[ind_l21])
 v10     = sum(vap[ind_l10])
 v01     = sum(vap[ind_l01])
 v12     = sum(vap[ind_l12])
 v23     = sum(vap[ind_l23])
 
 con_pha =array([c65,c54,c43,c32,c21,c10,c01,c12,c23]) ## condensed phase
 vap_pha =array([v65,v54,v43,v32,v21,v10,v01,v12,v23]) ## vapour phase
 
 ## total cond + vap
   
 all_pha = con_pha + vap_pha 
 
 return con_pha, all_pha;



file_258 = Dataset(path+'apin258.nc','r')
file_278 = Dataset(path+'apin278.nc','r')
file_293 = Dataset(path+'apin293.nc','r')
file_303 = Dataset(path+'apin303.nc','r')
file_313 = Dataset(path+'apin313.nc','r')

## calling the function 
c258,v258,es258,n258   = nc_read(file_258)
c278,v278,es278,n278   = nc_read(file_278)
c293,v293,es293,n293   = nc_read(file_293)
c303,v303,es303,n303   = nc_read(file_303)
c313,v313,es313,n313   = nc_read(file_313)


bas =array([1e-5,1e-4,1e-3,1e-2,1e-1,1e0,1e1,1e2,1e3])

## values from io_vbs
con258, all258 = io_vbs(c258,v258,es258)
con278, all278 = io_vbs(c278,v278,es278)
con293, all293 = io_vbs(c293,v293,es293)
con303, all303 = io_vbs(c303,v303,es303)
con313, all313 = io_vbs(c313,v313,es313)

z = linspace(0,0.6,9)

## figure 
fig = plt.figure(num=None, figsize=(18, 12), dpi=120, facecolor='w', edgecolor='k')
#plt.subplots(1,1, sharex=True, sharey=True)
barwidth=0.8

plt.subplot(2,3,1)
plt.bar(log10(bas),(all258/sum(all258)), width= barwidth, color = 'grey')
plt.bar(log10(bas),(con258/sum(all258)), width= barwidth,color = (0.3,0.9,0.4,0.6))

plt.fill_between([log10(1e-6),log10(0.0003)],0,0.6, facecolor= 'grey',alpha=0.3)
plt.fill_between([log10(0.00031),log10(0.3)],0,0.6,facecolor='r',alpha=0.3 )
plt.fill_between([log10(0.31),log10(300)],0,0.6,facecolor='g',alpha=0.3 )
plt.fill_between([log10(301),log10(1e4)],0,0.6,facecolor='c',alpha=0.3 )

plt.ylim(top=0.6)
plt.xlabel(r'$log_{10}$ C',fontsize=16)
plt.ylabel('Mass Fraction',fontsize=16)
plt.xticks([-5,-4,-3,-2,-1,0,1,2,3],fontsize=12)
plt.title('258.15 K',fontsize=14)



plt.subplot(2,3,2)
plt.bar(log10(bas),(all278/sum(all278)), width= barwidth, color = 'grey')
plt.bar(log10(bas),(con278/sum(all278)), width= barwidth,color = (0.3,0.9,0.4,0.6) )

plt.fill_between([log10(1e-6),log10(0.0003)],0,0.6, facecolor= 'grey',alpha=0.3)
plt.fill_between([log10(0.00031),log10(0.3)],0,0.6,facecolor='r',alpha=0.3 )
plt.fill_between([log10(0.31),log10(300)],0,0.6,facecolor='g',alpha=0.3 )
plt.fill_between([log10(301),log10(1e4)],0,0.6,facecolor='c',alpha=0.3 )

plt.ylim(top=0.6)
plt.xlabel(r'$log_{10}$ C',fontsize=16)
#plt.ylabel('Mass Fraction',fontsize=14)
plt.xticks([-5,-4,-3,-2,-1,0,1,2,3],fontsize=12)
plt.title('278.15 K',fontsize=14)


plt.subplot(2,3,3)
plt.bar(log10(bas),(all293/sum(all293)), width= barwidth, color = 'grey')
plt.bar(log10(bas),(con293/sum(all293)), width= barwidth, color = (0.3,0.9,0.4,0.6) )

plt.fill_between([log10(1e-6),log10(0.0003)],0,0.6, facecolor= 'grey',alpha=0.3)
plt.fill_between([log10(0.00031),log10(0.3)],0,0.6,facecolor='r',alpha=0.3 )
plt.fill_between([log10(0.31),log10(300)],0,0.6,facecolor='g',alpha=0.3 )
plt.fill_between([log10(301),log10(1e4)],0,0.6,facecolor='c',alpha=0.3 )

plt.ylim(top=0.6)
plt.xlabel(r'$log_{10}$ C',fontsize=16)
#plt.ylabel('Mass Fraction',fontsize=14)
plt.xticks([-5,-4,-3,-2,-1,0,1,2,3],fontsize=12)
plt.title('293.15 K',fontsize=14)


plt.subplot(2,3,4)
plt.bar(log10(bas),(all303/sum(all303)), width= barwidth, color = 'grey')
plt.bar(log10(bas),(con303/sum(all303)), width= barwidth,color = (0.3,0.9,0.4,0.6))

plt.fill_between([log10(1e-6),log10(0.0003)],0,0.6, facecolor= 'grey',alpha=0.3)
plt.fill_between([log10(0.00031),log10(0.3)],0,0.6,facecolor='r',alpha=0.3 )
plt.fill_between([log10(0.31),log10(300)],0,0.6,facecolor='g',alpha=0.3 )
plt.fill_between([log10(301),log10(1e4)],0,0.6,facecolor='c',alpha=0.3 )

plt.ylim(top=0.6)
plt.xlabel(r'$log_{10}$ C',fontsize=16)
plt.ylabel('Mass Fraction',fontsize=14)
plt.xticks([-5,-4,-3,-2,-1,0,1,2,3],fontsize=12)
plt.title('303.15 K',fontsize=14)


plt.subplot(2,3,5)
plt.bar(log10(bas),(all313/sum(all313)), width= barwidth, color = 'grey',label='Total Condensed + Vapour phase')
plt.bar(log10(bas),(con313/sum(all313)), width= barwidth, color = (0.3,0.9,0.4,0.6),label='Condensed phase' )

plt.fill_between([log10(1e-6),log10(0.0003)],0,0.6, facecolor= 'grey',alpha=0.3,label = 'ELVOC')
plt.fill_between([log10(0.00031),log10(0.3)],0,0.6,facecolor='r',alpha=0.3,label = 'LVOC' )
plt.fill_between([log10(0.31),log10(300)],0,0.6,facecolor='g',alpha=0.3,label = 'SVOC' )
plt.fill_between([log10(301),log10(1e4)],0,0.6,facecolor='c',alpha=0.3,label = 'IVOC' )

plt.ylim(top=0.6)
plt.xlabel(r'$log_{10}$ C',fontsize=16)
#plt.ylabel('Mass Fraction',fontsize=14)
plt.xticks([-5,-4,-3,-2,-1,0,1,2,3],fontsize=12)
plt.title('313.15 K',fontsize=14)

plt.subplots_adjust(wspace = 0.3 ,hspace = 0.3)
plt.figlegend(loc='lower right', bbox_to_anchor=(0.75, 0.2,0.05, 0.5),fontsize=16)

plt.suptitle(r'Volatility Basis set for $\alpha$-pinene (50ppb) - $O_3$ (50 ppb) ',fontsize=16)

plt.savefig('/home/local/carltonx/Work/Paper 1/plots_py/vbs_bar.png',bbox_inches = 'tight')
