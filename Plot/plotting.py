#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import numpy as np
import matplotlib.pyplot as plt
import sys
import pylab as pl 
#from mpl_toolkits.axes_grid.inset_locator import inset_axes
import matplotlib
#from matplotlib.pyplot import figure

print('This is a python script for plotting! ')

def plot_func(f1,f2,f3,f4,f5,f1_m,f2_m,f3_m,f4_m,f5_m,
               ft_h1,ft_h2,ft_h3,ft_h4,ft_h5,ft_m1,ft_m2,ft_m3,ft_m4,ft_m5,
               mw1,mw2,mw3,mw4,mw5):
 # constants
 Na     =  6.022E23
 ch_air =  2.47E19
 
 print('Plotting function for mass yields')
 
 ######################################################################
 ###################### FOR CHAMBER HOM RUNS ##################################
 ######################################################################
 print('HOM normal')
 
 # apinene
 C_oa_f1 = f1[:,5]/100 * (f1[:,4] * mw1 * 12.187 / 293.15) #ug/m3 mass concetration of organic aerosol in condensed phase
 dcoa_f1 = f1[:,4] * mw1  * 12.187 / 293.15 # ug/m3 reacted voc
 amf_f1  = C_oa_f1 / dcoa_f1 # yield

# bpinene
 C_oa_f2 = f2[:,5]/100 * (f2[:,4] * mw2 * 12.187 / 293.15)
 dcoa_f2 = f2[:,4] * mw2  * 12.187 / 293.15
 amf_f2  = C_oa_f2 / dcoa_f2
 
 # isoprene
 C_oa_f3 = f3[:,5]/100 * (f3[:,4] * mw3 * 12.187 / 293.15)
 dcoa_f3 = f3[:,4] * mw3  * 12.187 / 293.15
 amf_f3  = C_oa_f3 / dcoa_f3

 # bcary
 C_oa_f4 = f4[:,5]/100 * (f4[:,4] * mw4 * 12.187 / 293.15)
 dcoa_f4 = f4[:,4] * mw4  * 12.187 / 293.15
 amf_f4  = C_oa_f4 / dcoa_f4

 # limonene
 C_oa_f5 = f5[:,5]/100 * (f5[:,4] * mw5 * 12.187 / 293.15)
 dcoa_f5 = f5[:,4] * mw5  * 12.187 / 293.15
 amf_f5  = C_oa_f5 / dcoa_f5
 
 
 ######################################################################
 ###################### FOR FLOW TUBE HOM RUNS ########################
 ######################################################################
 
 print('HOM Flow Tube')
 
 # apinene
 C_oa_ft1 = ft_h1[:,5]/100 * (ft_h1[:,4] * mw1 * 12.187 / 293.15) #ug/m3 mass concetration of organic aerosol in condensed phase
 dcoa_ft1 = ft_h1[:,4] * mw1  * 12.187 / 293.15 # ug/m3 reacted voc
 amf_ft1  = C_oa_ft1 / dcoa_ft1 # yield

# bpinene
 C_oa_ft2 = ft_h2[:,5]/100 * (ft_h2[:,4] * mw2 * 12.187 / 293.15)
 dcoa_ft2 = ft_h2[:,4] * mw2  * 12.187 / 293.15
 amf_ft2  = C_oa_ft2 / dcoa_ft2
 
 # isoprene
 C_oa_ft3 = ft_h3[:,5]/100 * (ft_h3[:,4] * mw3 * 12.187 / 293.15)
 dcoa_ft3 = ft_h3[:,4] * mw3  * 12.187 / 293.15
 amf_ft3  = C_oa_ft3 / dcoa_ft3

 # bcary
 C_oa_ft4 = ft_h4[:,5]/100 * (ft_h4[:,4] * mw4 * 12.187 / 293.15)
 dcoa_ft4 = ft_h4[:,4] * mw4  * 12.187 / 293.15
 amf_ft4  = C_oa_ft4 / dcoa_ft4

 # limonene
 C_oa_ft5 = ft_h5[:,5]/100 * (ft_h5[:,4] * mw5 * 12.187 / 293.15)
 dcoa_ft5 = ft_h5[:,4] * mw5  * 12.187 / 293.15
 amf_ft5  = C_oa_ft5 / dcoa_ft5
 
 ######################################################################
 ###################### FOR FLOW TUBE MCM RUNS ########################
 ######################################################################
 
 print('MCM Flow Tube')
 
 # apinene
 C_oa_ft1_m = ft_m1[:,5]/100 * (ft_m1[:,4] * mw1 * 12.187 / 293.15) #ug/m3 mass concetration of organic aerosol in condensed phase
 dcoa_ft1_m = ft_m1[:,4] * mw1  * 12.187 / 293.15 # ug/m3 reacted voc
 amf_ft1_m  = C_oa_ft1_m / dcoa_ft1_m # yield

# bpinene
 C_oa_ft2_m = ft_m2[:,5]/100 * (ft_m2[:,4] * mw2 * 12.187 / 293.15)
 dcoa_ft2_m = ft_m2[:,4] * mw2  * 12.187 / 293.15
 amf_ft2_m  = C_oa_ft2_m / dcoa_ft2_m
 
 # isoprene
 C_oa_ft3_m = ft_m3[:,5]/100 * (ft_m3[:,4] * mw3 * 12.187 / 293.15)
 dcoa_ft3_m = ft_m3[:,4] * mw3  * 12.187 / 293.15
 amf_ft3_m  = C_oa_ft3_m / dcoa_ft3_m

 # bcary
 C_oa_ft4_m = ft_m4[:,5]/100 * (ft_m4[:,4] * mw4 * 12.187 / 293.15)
 dcoa_ft4_m = ft_m4[:,4] * mw4  * 12.187 / 293.15
 amf_ft4_m  = C_oa_ft4_m / dcoa_ft4_m

 # limonene
 C_oa_ft5_m = ft_m5[:,5]/100 * (ft_m5[:,4] * mw5 * 12.187 / 293.15)
 dcoa_ft5_m = ft_m5[:,4] * mw5  * 12.187 / 293.15
 amf_ft5_m  = C_oa_ft5_m / dcoa_ft5_m
 
 
 
 ######################################################################
 ###################### FOR MCM RUNS ##################################
 ######################################################################
 print('MCM normal')
 
 # apinene
 C_oa_f1_m = f1_m[:,5]/100 * (f1_m[:,4] * mw1 * 12.187 / 293.15) #ug/m3 mass concetration of organic aerosol in condensed phase
 dcoa_f1_m = f1_m[:,4] * mw1  * 12.187 / 293.15 # ug/m3 reacted voc
 amf_f1_m  = C_oa_f1_m / dcoa_f1_m # yield

# bpinene
 C_oa_f2_m = f2_m[:,5]/100 * (f2_m[:,4] * mw2 * 12.187 / 293.15)
 dcoa_f2_m = f2_m[:,4] * mw2  * 12.187 / 293.15
 amf_f2_m  = C_oa_f2_m / dcoa_f2_m
 
 # isoprene
 C_oa_f3_m = f3_m[:,5]/100 * (f3_m[:,4] * mw3 * 12.187 / 293.15)
 dcoa_f3_m = f3_m[:,4] * mw3  * 12.187 / 293.15
 amf_f3_m  = C_oa_f3_m / dcoa_f3_m

 # bcary
 C_oa_f4_m = f4_m[:,5]/100 * (f4_m[:,4] * mw4 * 12.187 / 293.15)
 dcoa_f4_m = f4_m[:,4] * mw4  * 12.187 / 293.15
 amf_f4_m  = C_oa_f4_m / dcoa_f4_m

# limonene
 C_oa_f5_m = f5_m[:,5]/100 * (f5_m[:,4] * mw5 * 12.187 / 293.15)
 dcoa_f5_m = f5_m[:,4] * mw5  * 12.187 / 293.15
 amf_f5_m  = C_oa_f5_m / dcoa_f5_m
 

 
############################ O3 PLOTS #############################
###################################################################
 
 fig =  plt.figure(num=None, figsize=(18, 12), dpi=80, facecolor='w', edgecolor='k')
 
 #fig = plt.subplots(1,2,sharex= True)

 ax1 = plt.subplot(211)
 
 ### chamber
 plt.scatter(C_oa_f1[np.where(f1[:,2] != 0)],amf_f1[np.where(f1[:,2] != 0)], 50,
             color='r',marker='o',label=r'$\alpha$-pinene (Chamber)')
 plt.scatter(C_oa_f2[np.where(f2[:,2] != 0)],amf_f2[np.where(f2[:,2] != 0)], 50, 
             c='b',marker='s',label=r'$\beta$-pinene (Chamber)')
 plt.scatter(C_oa_f4[np.where(f4[:,2] != 0)],amf_f4[np.where(f4[:,2] != 0)], 50,
             c='k',marker='^',label=r'$\beta$-caryophyllene (Chamber)')
 plt.scatter(C_oa_f5[np.where(f5[:,2] != 0)],amf_f5[np.where(f5[:,2] != 0)], 50,
             c='g',marker='X',label='limonene (Chamber)')
 
 ### flowtube
 plt.scatter(C_oa_ft1[np.where(ft_h1[:,2] != 0)],amf_ft1[np.where(ft_h1[:,2] != 0)], 70, ## FT
             facecolor='none',edgecolor='r', marker='o',label=r'$\alpha$-pinene (Flow-Tube)')
 plt.scatter(C_oa_ft2[np.where(ft_h2[:,2] != 0)],amf_ft2[np.where(ft_h2[:,2] != 0)], 70, 
             facecolor='none',edgecolor='b',marker='s',label=r'$\beta$-pinene (Flow-Tube)')
 plt.scatter(C_oa_ft4[np.where(ft_h4[:,2] != 0)],amf_ft4[np.where(ft_h4[:,2] != 0)], 70,
             facecolor='none',edgecolor='m',marker='^',label=r'$\beta$-caryophyllene (Flow-Tube)')
 plt.scatter(C_oa_ft5[np.where(ft_h5[:,2] != 0)],amf_ft5[np.where(ft_h5[:,2] != 0)], 70,
             facecolor='none',edgecolor='g',marker='X',label='limonene (Flow-Tube)')
  
  
 handles, labels = ax1.get_legend_handles_labels()
 #plt.figlegend(scatterpoints = 1,loc=(0.95, 0.5), fontsize=15)
 plt.legend(loc='center', bbox_to_anchor=(1.15, 0.), shadow=True, ncol=1, fontsize=15)

 plt.ylabel(r'$Y_{COMB}$',fontsize = 18)
 plt.xticks(fontsize = 16)
 plt.yticks(fontsize = 16)
 plt.xscale('log')
 plt.grid(True)
 
 
 
 ax2 = plt.subplot(212,sharex=ax1) 
 ## chamber
 plt.scatter(C_oa_f1[np.where(f1_m[:,2] != 0)],(amf_f1[np.where(f1[:,2] != 0)]-amf_f1_m[np.where(f1_m[:,2] != 0)]), 50,
             color='r',marker='o',label=r'$\alpha$-pinene')
# plt.scatter(C_oa_f2[np.where(f2_m[:,2] != 0)],(amf_f2[np.where(f2[:,2] != 0)]-amf_f2_m[np.where(f1_m[:,2] != 0)]), 50, 
#             c='b',marker='s',label=r'$\beta$-pinene')
# plt.scatter(C_oa_f4[np.where(f4_m[:,2] != 0)],(amf_f4[np.where(f4[:,2] != 0)]-amf_f4_m[np.where(f4_m[:,2] != 0)]), 50,
#            c='m',marker='^',label=r'$\beta$-caryophyllene')
 plt.scatter(C_oa_f5[np.where(f5_m[:,2] != 0)],(amf_f5[np.where(f5[:,2] != 0)]-amf_f5_m[np.where(f5_m[:,2] != 0)]), 50,
             c='g',marker='X',label='limonene')
 
 ## flowtube
 plt.scatter(C_oa_ft1[np.where(ft_m1[:,2] != 0)],(amf_ft1[np.where(ft_h1[:,2] != 0)]-amf_ft1_m[np.where(ft_m1[:,2] != 0)]), 70,
             facecolor='none',edgecolor='r',marker='o',label=r'$\alpha$-pinene')
# plt.scatter(C_oa_ft2[np.where(ft_m2[:,2] != 0)],(amf_ft2[np.where(ft_h2[:,2] != 0)]-amf_ft2_m[np.where(ft_m2[:,2] != 0)]), 70, 
#             facecolor='none',edgecolor='b',marker='s',label=r'$\beta$-pinene')
# plt.scatter(C_oa_ft4[np.where(ft_m4[:,2] != 0)],(amf_ft4[np.where(ft_h4[:,2] != 0)]-amf_ft4_m[np.where(ft_m4[:,2] != 0)]), 70,
#            facecolor='none',edgecolor='m',marker='^',label=r'$\beta$-caryophyllene')
 plt.scatter(C_oa_ft5[np.where(ft_m5[:,2] != 0)],(amf_ft5[np.where(ft_h5[:,2] != 0)]-amf_ft5_m[np.where(ft_m5[:,2] != 0)]), 70,
             facecolor='none',edgecolor='g',marker='X',label='limonene')
 
# plt.legend(scatterpoints = 1,loc='upper left',fontsize=15)

 plt.xlabel(r'SOA mass loadings$(\mu$g/$m^3$)', fontsize =20)
 plt.ylabel(r'$Y_{COMB}$ - $Y_{MCM}$',fontsize = 18)
 plt.yticks(fontsize = 16)
 plt.xticks(fontsize = 16)
 plt.grid(True)
 plt.setp(ax2.get_xticklabels(), visible=True)
  
 plt.subplots_adjust(wspace = 0.3 ,hspace = 0.3)
 plt.suptitle(r'BVOCs - $O_3$ dependence for COMB_Mechanism',fontsize=18)
 plt.savefig('/home/local/carltonx/Work/Paper 1/plots_py/bvoc-o3.png',bbox_inches = 'tight')

################################ OH plots #####################################
###############################################################################̈́
 
 fig = plt.figure(num=None, figsize=(18, 12), dpi=80, facecolor='w', edgecolor='k')

 ax1 = plt.subplot(211)
 plt.scatter(C_oa_f1[np.where(f1[:,1] != 0)],amf_f1[np.where(f1[:,1] != 0)], 50,
              c='r',marker='o',label=r'$\alpha$-pinene (Chamber)')
 plt.scatter(C_oa_f2[np.where(f2[:,1] != 0)],amf_f2[np.where(f2[:,1] != 0)], 50,
            c='b',marker='s',label=r'$\beta$-pinene (Chamber)')
 plt.scatter(C_oa_f3[np.where(f3[:,1] != 0)],amf_f3[np.where(f3[:,1] != 0)], 50,
             c='k',marker='D', label = 'Isoprene (Chamber)')
 plt.scatter(C_oa_f4[np.where(f4[:,1] != 0)],amf_f4[np.where(f4[:,1] != 0)], 50,
             c='m',marker='^',label= r'$\beta$-caryophyllene (Chamber)')
 plt.scatter(C_oa_f5[np.where(f5[:,1] != 0)],amf_f5[np.where(f5[:,1] != 0)], 50,
             c='g',marker='X',label='limonene (Chamber)')

 plt.scatter(C_oa_ft1[np.where(ft_h1[:,1] != 0)],amf_ft1[np.where(ft_h1[:,1] != 0)], 70,
             facecolor='none',edgecolor='r',marker='o',label=r'$\alpha$-pinene (Flow-Tube)')
 plt.scatter(C_oa_ft2[np.where(ft_h2[:,1] != 0)],amf_ft2[np.where(ft_h2[:,1] != 0)], 70,
            facecolor='none',edgecolor='b',marker='s',label=r'$\beta$-pinene (Flow-Tube)')
 plt.scatter(C_oa_ft3[np.where(ft_h3[:,1] != 0)],amf_ft3[np.where(ft_h3[:,1] != 0)], 70,
             facecolor='none',edgecolor='k',marker='D', label = 'Isoprene (Flow-Tube)')
 plt.scatter(C_oa_ft4[np.where(ft_h4[:,1] != 0)],amf_ft4[np.where(ft_h4[:,1] != 0)], 70,
            facecolor='none',edgecolor='m',marker='^',label= r'$\beta$-caryophyllene (Flow-Tube)')
 plt.scatter(C_oa_ft5[np.where(ft_h5[:,1] != 0)],amf_ft5[np.where(ft_h5[:,1] != 0)], 70,
            facecolor='none',edgecolor='g',marker='X',label='limonene (Flow-Tube)') 
  
 plt.legend(loc='center', bbox_to_anchor=(1.15, 0.), shadow=True, ncol=1, fontsize=15)
 
 plt.ylabel(r'$Y_{COMB}$',fontsize=18)
 plt.xticks(fontsize = 16)
 plt.yticks(fontsize = 16)
 plt.xscale('log')
 plt.grid(True)

 
 ax2 = plt.subplot(212,sharex=ax1) 
 
 ### chamber
 plt.scatter(C_oa_f1[np.where(f1_m[:,1] != 0)],(amf_f1[np.where(f1[:,1] != 0)]-amf_f1_m[np.where(f1_m[:,1] != 0)]), 50,
             color='r',marker='o',label=r'$\alpha$-pinene')
 plt.scatter(C_oa_f2[np.where(f2_m[:,1] != 0)],(amf_f2[np.where(f2[:,1] != 0)]-amf_f2_m[np.where(f1_m[:,1] != 0)]), 50, 
             c='b',marker='s',label=r'$\beta$-pinene')
# plt.scatter(C_oa_f3[np.where(f3_m[:,1] != 0)],(amf_f3[np.where(f3[:,1] != 0)]-amf_f3_m[np.where(f3_m[:,1] != 0)]), 50, 
#             c='k',marker='D',label='Isoprene')
# plt.scatter(C_oa_f4[np.where(f4_m[:,1] != 0)],(amf_f4[np.where(f4[:,1] != 0)]-amf_f4_m[np.where(f4_m[:,1] != 0)]), 50,
#            c='m',marker='^',label=r'$\beta$-caryophyllene')
 plt.scatter(C_oa_f5[np.where(f5_m[:,1] != 0)],(amf_f5[np.where(f5[:,1] != 0)]-amf_f5_m[np.where(f5_m[:,1] != 0)]), 50,
             c='g',marker='X',label='limonene')
 
 
 ## flowtube
 plt.scatter(C_oa_ft1[np.where(ft_m1[:,1] != 0)],(amf_ft1[np.where(f1[:,1] != 0)]-amf_ft1_m[np.where(f1_m[:,1] != 0)]), 50,
             facecolor='none',edgecolor='r',marker='o',label=r'$\alpha$-pinene')
 plt.scatter(C_oa_ft2[np.where(ft_m2[:,1] != 0)],(amf_ft2[np.where(f2[:,1] != 0)]-amf_ft2_m[np.where(f1_m[:,1] != 0)]), 50, 
             facecolor='none',edgecolor='b',marker='s',label=r'$\beta$-pinene')
# plt.scatter(C_oa_ft3[np.where(ft_m3[:,1] != 0)],(amf_ft3[np.where(f3[:,1] != 0)]-amf_ft3_m[np.where(f3_m[:,1] != 0)]), 50, 
#             facecolor='none',edgecolor='k',marker='D',label='Isoprene')
# plt.scatter(C_oa_ft4[np.where(ft_m4[:,1] != 0)],(amf_ft4[np.where(f4[:,1] != 0)]-amf_ft4_m[np.where(f4_m[:,1] != 0)]), 50,
#            facecolor='none',edgecolor='m',marker='^',label=r'$\beta$-caryophyllene')
 plt.scatter(C_oa_ft5[np.where(ft_m5[:,1] != 0)],(amf_ft5[np.where(f5[:,1] != 0)]-amf_ft5_m[np.where(f5_m[:,1] != 0)]), 50,
             facecolor='none',edgecolor='g',marker='X',label='limonene')
 
 
 #plt.legend(scatterpoints = 1,loc='upper left',fontsize=15)

 plt.xlabel(r'SOA mass loadings$(\mu$g/$m^3$)', fontsize =20)
 plt.ylabel(r'$Y_{COMB}$ - $Y_{MCM}$',fontsize = 18)
 plt.xticks(fontsize = 16)
 plt.yticks(fontsize = 16)
 plt.grid(True)
 
 plt.subplots_adjust(wspace = 0.3 ,hspace = 0.3)
 plt.suptitle('BVOC - OH dependence for COMB_Mechanism',fontsize=18)
 plt.savefig('/home/local/carltonx/Work/Paper 1/plots_py/bvoc-oh.png',bbox_inches = 'tight')

 plt.show()


 return;
 
 # temp plots
def temp_plot(f1,f2,f3,f4,f5,t1,t2,t3,t4,t5,mw1):
 
 print('Temperature dependence function')

 #258
 C_oa_f1 = f1[:,5]/100 * (f1[:,4] * mw1 * 12.187 / t1) #ug/m3 mass concetration of organic aerosol in condensed phase
 dcoa_f1 = f1[:,4] * mw1  * 12.187 / t1 # ug/m3 reacted voc
 amf_f1  = C_oa_f1 / dcoa_f1 # yield

 #278
 C_oa_f2 = f2[:,5]/100 * (f2[:,4] * mw1 * 12.187 / t2)
 dcoa_f2 = f2[:,4] * mw1  * 12.187 / t2
 amf_f2  = C_oa_f2 / dcoa_f2

#293
 C_oa_f3 = f3[:,5]/100 * (f3[:,4] * mw1 * 12.187 / t3)
 dcoa_f3 = f3[:,4] * mw1  * 12.187 / t3
 amf_f3  = C_oa_f3 / dcoa_f3

#303
 C_oa_f4 = f4[:,5]/100 * (f4[:,4] * mw1 * 12.187 / t4)
 dcoa_f4 = f4[:,4] * mw1  * 12.187 / t4
 amf_f4  = C_oa_f4 / dcoa_f4

 #313
 C_oa_f5 = f5[:,5]/100 * (f5[:,4] * mw1 * 12.187 / t5)
 dcoa_f5 = f5[:,4] * mw1  * 12.187 / t5
 amf_f5  = C_oa_f5 / dcoa_f5

 
##Temp PLOTS
 
# fig = plt.figure(1) 
 plt.figure(num=None, figsize=(18, 12), dpi=80, facecolor='w', edgecolor='k')

 plt.scatter(C_oa_f1[np.where(f1[:,2] != 0)],amf_f1[np.where(f1[:,2] != 0)], 50,
              c='r',marker='o')
 plt.scatter(C_oa_f2[np.where(f2[:,2] != 0)],amf_f2[np.where(f2[:,2] != 0)], 50,
             c='b',marker='s')
 plt.scatter(C_oa_f3[np.where(f3[:,2] != 0)],amf_f3[np.where(f3[:,2] != 0)], 50,
             c='k',marker='D')
 plt.scatter(C_oa_f4[np.where(f4[:,2] != 0)],amf_f4[np.where(f4[:,2] != 0)], 50,
             c='m',marker='^')
 plt.scatter(C_oa_f5[np.where(f5[:,2] != 0)],amf_f5[np.where(f5[:,2] != 0)], 50,
             c='g',marker='X')
  
 plt.legend(('{:06.2f}'.format(t1)+'K','{:06.2f}'.format(t2)+'K','{:06.2f}'.format(t3)+'K','{:06.2f}'.format(t4)+'K',
              '{:06.2f}'.format(t5)+'K'),scatterpoints = 1,loc='upper left',fontsize=16)

 plt.xlabel(r'SOA mass loadings$(\mu$g/$m^3$)',fontsize=20)
 plt.xticks(fontsize=14, rotation=0)
 plt.ylabel('Mass yields',fontsize=20)
 plt.yticks(fontsize=14, rotation=0)
 plt.xscale('log')
 plt.grid(True)
 plt.title(r'$\alpha$-pinene - $O_3$ Temperature dependence',fontsize=24)
 plt.savefig('/home/local/carltonx/Work/Paper 1/plots_py/apin-temp.png')

 plt.show()


 return;
 
def nox_plot(f1,f2,f3,n1,n2,n3,t1,mw1):
 
 print('Temperature dependence function')

 #2.5ppb
 C_oa_f1 = f1[:,5]/100 * (f1[:,4] * mw1 * 12.187 / t1) #ug/m3 mass concetration of organic aerosol in condensed phase
 dcoa_f1 = f1[:,4] * mw1  * 12.187 / t1 # ug/m3 reacted voc
 amf_f1  = C_oa_f1 / dcoa_f1 # yield

 #12.5ppb
 C_oa_f2 = f2[:,5]/100 * (f2[:,4] * mw1 * 12.187 / t1)
 dcoa_f2 = f2[:,4] * mw1  * 12.187 / t1
 amf_f2  = C_oa_f2 / dcoa_f2

#25 ppb
 C_oa_f3 = f3[:,5]/100 * (f3[:,4] * mw1 * 12.187 / t1)
 dcoa_f3 = f3[:,4] * mw1  * 12.187 / t1
 amf_f3  = C_oa_f3 / dcoa_f3

 
##NOx plots
 
# fig = plt.figure(1) 
 plt.figure(num=None, figsize=(18, 12), dpi=80, facecolor='w', edgecolor='k')

 plt.scatter(C_oa_f1[np.where(f1[:,2] != 0)],amf_f1[np.where(f1[:,2] != 0)], 50,
              c='r',marker='o')
 plt.scatter(C_oa_f2[np.where(f2[:,2] != 0)],amf_f2[np.where(f2[:,2] != 0)], 50,
             c='b',marker='s')
 plt.scatter(C_oa_f3[np.where(f3[:,2] != 0)],amf_f3[np.where(f3[:,2] != 0)], 50,
             c='k',marker='D')
 
  
 plt.legend(('{:03.1f}'.format(n1)+' ppb','{:03.1f}'.format(n2)+' ppb','{:03.1f}'.format(n3)+' ppb'),
             scatterpoints = 1,loc='upper left',fontsize=16)

 plt.xlabel(r'SOA mass loadings$(\mu$g/$m^3$)',fontsize=20)
 plt.xticks(fontsize=14, rotation=0)
 plt.ylabel('Mass yields',fontsize=20)
 plt.yticks(fontsize=14, rotation=0)
 plt.xscale('log')
 plt.grid(True)
 plt.title(r'$\alpha$-pinene - $O_3$ - $NO_x$ dependence',fontsize=24)
 plt.savefig('/home/local/carltonx/Work/Paper 1/plots_py/apin-nox.png')

 plt.show()


 return;


path_hom      = '/home/local/carltonx/Work/Malte_box/Project_runs/sep_update_res/Hom_normal/'
path_mcm      = '/home/local/carltonx/Work/Malte_box/Project_runs/sep_update_res/Mcm_normal/'
path_t        = '/home/local/carltonx/Work/Malte_box/Project_runs/sep_update_res/Temp_runs/'
path_n        = '/home/local/carltonx/Work/Malte_box/Project_runs/sep_update_res/Nox_runs/'
path_ft_hom   = '/home/local/carltonx/Work/Malte_box/Project_runs/sep_update_res/FT_hom/'
path_ft_mcm   = '/home/local/carltonx/Work/Malte_box/Project_runs/sep_update_res/FT_mcm/'


#NORMAL RUNS FOR HOM
apin_hom = np.loadtxt(path_hom+'apinene.dat')
bpin_hom = np.loadtxt(path_hom+'bpinene.dat')
isop_hom = np.loadtxt(path_hom+'isoprene.dat')
bcar_hom = np.loadtxt(path_hom+'bcary.dat')
limo_hom = np.loadtxt(path_hom+'limonene.dat')

## MCM RUNS
apin_mcm = np.loadtxt(path_mcm+'apinene_mcm.dat')
bpin_mcm = np.loadtxt(path_mcm+'bpinene_mcm.dat')
bcar_mcm = np.loadtxt(path_mcm+'bcary_mcm.dat')
isop_mcm = np.loadtxt(path_mcm+'isoprene_mcm.dat')
limo_mcm = np.loadtxt(path_mcm+'limonene_mcm.dat')

## flow tube runs for hom#

apin_ft_h = np.loadtxt(path_ft_hom+'apinene_ft_hom.dat')
bpin_ft_h = np.loadtxt(path_ft_hom+'bpinene_ft_hom.dat')
bcar_ft_h = np.loadtxt(path_ft_hom+'bcary_ft_hom.dat')
isop_ft_h = np.loadtxt(path_ft_hom+'isoprene_ft_hom.dat')
limo_ft_h = np.loadtxt(path_ft_hom+'limonene_ft_hom.dat')


## flow tube runs for hom#

apin_ft_m = np.loadtxt(path_ft_mcm+'apinene_ft_mcm.dat')
bpin_ft_m = np.loadtxt(path_ft_mcm+'bpinene_ft_mcm.dat')
bcar_ft_m = np.loadtxt(path_ft_mcm+'bcary_ft_mcm.dat')
isop_ft_m = np.loadtxt(path_ft_mcm+'isoprene_ft_mcm.dat')
limo_ft_m = np.loadtxt(path_ft_mcm+'limonene_ft_mcm.dat')

# temp runs
apin_258 = np.loadtxt(path_t+'apinene258.dat')
apin_278 = np.loadtxt(path_t+'apinene278.dat')
apin_303 = np.loadtxt(path_t+'apinene303.dat')
apin_313 = np.loadtxt(path_t+'apinene313.dat')

# nox runs
apin_125 = np.loadtxt(path_n+'apinene125.dat')
apin_250 = np.loadtxt(path_n+'apinene250.dat')



plot_func(apin_hom,bpin_hom,isop_hom,bcar_hom,limo_hom,apin_mcm,bpin_mcm,isop_mcm,bcar_mcm,limo_mcm,
           apin_ft_h,bpin_ft_h,isop_ft_h,bcar_ft_h,limo_ft_h, apin_ft_m,bpin_ft_m,isop_ft_m,bcar_ft_m,limo_ft_m
           ,136.23,136.23,68.12,204.36,136.24)



#temp_plot(apin_258,apin_278,apin_hom,apin_303,apin_313, 258.15,278.15,293.15, 303.15, 313.15, 136.23)
#nox_plot(apin_hom,apin_125,apin_250,2.5,12.5,25,293.15,136.23)