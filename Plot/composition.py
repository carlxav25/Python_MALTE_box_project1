#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:08:42 2018

@author: carltonx
"""

from numpy import *
from ncread import nc_read
from netCDF4 import *
import matplotlib.pyplot as plt

#print(np.__version__) 

path       = '/home/local/carltonx/Work/Malte_box/Project_runs/netcdf_input/'
path_vap   = '/home/local/carltonx/Work/Malte_box/Project_runs/malte_box/Malte_in/Box/Test1234/new_chem/'

def calc_plot(conc,vap_prop,vap_name,vap_oc,num,t1):
 
 # index for values > 0.25 ug/m3
 ind        = where(conc>=0.25)
# print(ind)

 
 par       = conc[ind]                                                       # particle phase
 mw        = vap_prop[ind,0].T                                               # Molecular weight
 cont      = sum(par)/sum(conc) * 100                                        # contribution by the selected compounds 
 oc_sc     = conc[ind]                                                       # O:C ratio of selected compounds
 names_sc  = vap_name[ind]                                                   # names of selected compounds
 h_ind     = [i for i, s in enumerate(names_sc) if 'HOM' in s]               # HOM index for selected compound
 m_ind     = [i for i, s in enumerate(names_sc) if 'HOM' not in s]           # MCM index for selected compounds
 hom_sc    = names_sc[h_ind]                                                 # names of selcted HOM compounds
 mcm_sc    = names_sc[m_ind]                                                 # names of selected MCM compounds                
 mw_mcm    = mw[m_ind]                                                       # Mol. Wei of MCM compounds
 mw_hom    = mw[h_ind]                                                       # Mol. Wei of HOM compounds 
 par_cont  = par / sum(conc) * 100
# print(par_cont)
 mcm_ug    = par[m_ind]                                                      # ug/m3 contribution by MCM compounds
 hom_ug    = par[h_ind]                                                      # ug/m3 contribution by HOM compounds
 c_mol     = vap_oc[ind,1].T                                                 # C molecules
 o_mol     = vap_oc[ind,2].T                                                 # O molecules
 n_mol     = vap_oc[ind,3].T                                                 # N molecules 
 c_mol_h   = c_mol[h_ind].T
 o_mol_h   = o_mol[h_ind].T
 n_mol_h   = n_mol[h_ind].T
 
 mcm_cont = sum(mcm_ug)/sum(par) * 100
 hom_cont = sum(hom_ug)/sum(par) * 100
# print(c_mol_h)
# print(o_mol_h)
# print(n_mol_h)
# print(mw.shape)
 
 h_mol   = round_(mw.T - (c_mol*12 + o_mol*16 + n_mol*14))
 h_mol_h = round_(mw_hom.T - (c_mol_h*12 + o_mol_h*16 + n_mol_h*14))
# print((n_mol_h))
  
 #### for converting to compound names
 comp_hom =[]
 for i in range(len(c_mol_h.T)):
     if any(abs(n_mol_h[0,i]) > 0):  
      comp_hom.append('C{:1.0f}H{:1.0f}O{:1.0f}N{:1.0f}'.format(c_mol_h[0,i],h_mol_h[0,i], o_mol_h[0,i], n_mol_h[0,i]))
     else:  
      comp_hom.append('C{:1.0f}H{:1.0f}O{:1.0f}'.format(c_mol_h[0,i],h_mol_h[0,i], o_mol_h[0,i]))
      
 final_name = concatenate((mcm_sc,comp_hom))     # name list for final names strings

 print(np.array(mw).shape)     
 print(final_name.shape)
 
 ## O:C ratios
 
 oc = (np.multiply(np.array(num[ind]), np.array(vap_oc[ind,0]))) / sum(num[ind])
# print(vap_oc[ind,0].shape)
 print(oc.T.shape)
 print(size(oc))
 print(par_cont.shape)
 

 
 #print(comp_hom.shape)
 # for all compounds 
 hom_ind       = [i for i, s in enumerate(vap_name[:-1]) if 'HOM' in s]
 mcm_ind       = [i for i, s in enumerate(vap_name[:-1]) if 'HOM' not in s]
 nm_mcm_all    = vap_name[mcm_ind]                                            # Name of MCM compounds 
 nm_hom_all    = vap_name[hom_ind]                                            # Name of HOM compounds   
 hom_abs       = sum(conc[hom_ind])                                           # contribution by all HOM compounds in ug/m3
 mcm_abs       = sum(conc[mcm_ind])                                           # contribution by all MCM compounds in ug/m3
 
 
 ##########figure###################################
 
 fig = plt.figure(num=None, figsize=(18, 12), dpi=120, facecolor='w', edgecolor='k')
 ax1 = fig.add_subplot(111)
 ax2 = ax1.twiny()

 
 ax1.bar(mcm_sc,mcm_ug,width=0.5,label='Total MCM compunds contribution (%) = '+'{:02.2f}'.format(mcm_cont))
 ax1.bar(comp_hom,hom_ug,width=0.5,label='Total PRAM compunds contribution (%) = '+'{:02.2f}'.format(hom_cont))
 
## for ax1 axis
 ax1.set_ylabel(r'SOA mass loadings $(\mu$g/$m^3$)',fontsize=20)
 ax1.tick_params('y',rotation=0)
 ax1.set_xlabel('Compounds',fontsize=18)
 ax1.tick_params('x', rotation=90,labelcolor='k')
 ax1.set_xticklabels(final_name,fontsize=12)
 plt.yticks(fontsize=14)
 
 ax2.set_xlim(ax1.get_xlim())
 ax2.set_xticks(ax1.get_xticks())
 
### second axis
 fig.subplots_adjust(bottom=0.15)
 ax2.set_xticklabels(mw)
 ax2.xaxis.set_ticks_position('bottom') # set the position of the second x-axis to bottom
 ax2.xaxis.set_label_position('bottom') # set the position of the second x-axis to bottom
 ax2.spines['bottom'].set_position(("axes", -0.2)) # set_position(('outward', 36))
 ax2.tick_params('x',rotation=90, labelcolor = 'blue')
 ax2.set_xlabel('Molecular weight',fontsize=18)
 
 plt.xticks(fontsize=12)
 ax1.legend(fontsize=14)#('Total contribution by PRAM + MCM (%)'+'{:06.2f}'.format(cont)),
            #loc='upper right',fontsize=10)
 
 plt.title(r'$\alpha$-pinene (50ppb) - $O_3$ (50 ppb) at '+'{:06.2f}'.format(t1) + 'K, '\
           'Total contribution by COMB_Mech (%) = '+'{:04.2f}'.format(cont),fontsize=20)
 
 plt.savefig('/home/local/carltonx/Work/Paper 1/plots_py/comp'+'{:03.0f}'.format(t1)+'.png',bbox_inches = 'tight')

 plt.show()
 
 
 return;
    
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
 
vap_prop = loadtxt(path_vap+'Vapour_properties.dat')
vap_name = genfromtxt(path_vap+'Vapour_names.dat',dtype='str')
vap_oc   = loadtxt(path_vap+'Vapour_O_C_ratio_Carlton.dat')

calc_plot(c258,vap_prop,vap_name,vap_oc,n258,258.15)
#calc_plot(c278,vap_prop,vap_name,vap_oc,278.15)
#calc_plot(c293,vap_prop,vap_name,vap_oc,293.15)
#calc_plot(c303,vap_prop,vap_name,vap_oc,303.15)
#calc_plot(c313,vap_prop,vap_name,vap_oc,313.15)