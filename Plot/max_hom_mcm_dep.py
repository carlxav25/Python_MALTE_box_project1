#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 16:16:02 2018

@author: carltonx
"""
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

path = '/home/local/carltonx/Work/Malte_box/Project_runs/sep_update_res/'
file = loadtxt(path+'max_yield.dat')


i_oh = [i for i,x in enumerate(file[:,1]) if x == 10]
i_o3 = [i for i,x in enumerate(file[:,1]) if x == 20]


hom_oh = file[i_oh,3]
mcm_oh = file[i_oh,4]

hom_o3 = file[i_o3,3]
mcm_o3 = file[i_o3,4]

oh_data = np.array([hom_oh,mcm_oh]).T
o3_data = np.array([hom_o3,mcm_o3]).T

oh = np.reshape(oh_data,(3,4)).T
o3 = np.reshape(o3_data,(3,4)).T

fig = plt.figure(num=None, figsize=(18, 14), dpi=120, facecolor='w', edgecolor='k')
barwidth = 0.8
tickpos  = [2.5,7.5,12.5]


r1 = [1,6,11]
r2 = [2,7,12]
r3 = [3,8,13]
r4 = [4,9,14]

ax1 = plt.subplot(211)
plt.bar(r1,oh[0,:], width = barwidth,color=(0.3,0.1,0.4,0.6),label='Total PRAM contribution(%)-Chamber runs' )
plt.bar(r2,oh[1,:], width = barwidth, color='orange',label='Total MCM contribution(%)-Chamber runs')
plt.bar(r3,oh[2,:], width = barwidth, color=(0.3,0.9,0.4,0.6),label='Total PRAM contribution(%)-Flow-tube runs')
plt.bar(r4,oh[3,:], width = barwidth, color='grey',label='Total MCM contribution(%)-Flow-tube runs') 

#plt.xlabel('Compounds', fontsize=12)
plt.ylabel('Contribution to SOA mass yields(%)', fontsize = 14)
plt.xticks(tickpos,[r'$\alpha$-pinene' ,r'$\beta$-pinene','Limonene'],fontsize=14)
plt.yticks(fontsize = 16)
plt.title('OH',fontsize = 16)
plt.grid(False)

plt.legend(loc='center left',bbox_to_anchor=(1.0, 0.5,0.1,-0.4), shadow=True, ncol=1, fontsize=14) 

ax2 = plt.subplot(212,sharex=ax1)
plt.bar(r1,o3[0,:], width = barwidth,color=(0.3,0.1,0.4,0.6),label='Total PRAM contribution(%)-Chamber runs' )
plt.bar(r2,o3[1,:], width = barwidth, color='orange',label='Total MCM contribution(%)-Chamber runs')
plt.bar(r3,o3[2,:], width = barwidth, color=(0.3,0.9,0.4,0.6),label='Total PRAM contribution(%)-Flow-tube runs')
plt.bar(r4,o3[3,:], width = barwidth, color='grey',label='Total MCM contribution(%)-Flow-tube runs') 
plt.title(r'$O_3$',fontsize = 16)


#plt.legend(loc='center', bbox_to_anchor=(1.15, 0.), shadow=True, ncol=1, fontsize=12)
plt.xlabel('Compounds', fontsize=15)
plt.ylabel('Contribution to SOA mass yields(%)', fontsize = 14)
plt.xticks(tickpos,[r'$\alpha$-pinene' ,r'$\beta$-pinene','Limonene'],fontsize=14)
plt.yticks(fontsize = 16)
plt.grid(False)
plt.suptitle('Relative contribution by PRAM and MCM compounds', fontsize = 18)

plt.subplots_adjust(wspace = 0. ,hspace = 0.3)
 
plt.savefig('/home/local/carltonx/Work/Paper 1/plots_py/max_yields_bar.png',bbox_inches = 'tight')