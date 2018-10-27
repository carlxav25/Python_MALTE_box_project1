#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:37:42 2018

@author: carltonx
"""
from numpy import *
from netCDF4 import *

def nc_read(nc):
 
# print(nc)    
 num_conc = nc.variables['number_concentration']
   #print num_conc.units
   #print(num_conc.shape) 

 rad = nc.variables['radius']
  #print rad.units
  #print rad.shape 

 molar_mass = nc.variables['molarmass']
#print or_dry_rad.units
# print('Molar_mass shape'+str(molar_mass[:-2].shape))

 time_in_units = nc.variables['time_in_units']
#print time_in_units.units
# print('time'+str(time_in_units.shape))

 vol_conc = nc.variables['volume_concentration']
#print vol_conc.units
# print(vol_conc.shape) 
                               
 vap_conc = nc.variables['vapor_concentration']
 #print vap_conc.units
 #print(vap_conc.shape) 

 vap_den = nc.variables['vapor_density']
 #print vap_den.units
 #print(vap_den.shape) 
  
  
 sat_conc = nc.variables['saturation_concentration']
 #print vap_den.units
 #print vap_den.shape 

 (tim, com)  = vap_conc.shape
 (tim, sec)  = rad.shape
# time = time_in_units[:]//43200
 
# print('tim'+str(tim)+'and com'+str(com))
 ch_air = 2.47E19
 Na     = 6.022E23
 
# print(sum(vol_conc[-1,0:com-2,:].T*vap_den[:-2]).shape)
# print(vap_den[:-2].T.shape)

 cond_phase   = sum((vol_conc[-1,0:com-2,:].T * vap_den[:-2]),0)*1E-9    #ug/m3
# print(cond_phase.shape)
 vap_phase    = vap_conc[-1,0:com-2] * molar_mass[:-2] / Na *1E6     #ug/m3
 #print(vap_phase.shape)
 eff_sat_con  = sat_conc[-1,0:com-2] * molar_mass[:-2] / Na *1E6     #ug/m3
 #print(eff_sat_con.shape)
 num_conc_m3  = cond_phase / molar_mass[:-2] * Na *1E-6
# print(num_conc_m3.shape)
# print(type(molar_mass))
 return cond_phase,vap_phase,eff_sat_con, num_conc_m3 ;

