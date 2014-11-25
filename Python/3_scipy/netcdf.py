#!/usr/bin/env python
#
# Generates a netcdf file.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

import numpy as np
from scipy.io import netcdf

#Create a new netCDF file
f = netcdf.netcdf_file('simple.nc', 'w')
f.history = 'Created for a test'
f.createDimension('time', 10)
time = f.createVariable('time', 'i', ('time',))
time[:] = np.arange(10)
time.units = 'days since 2008-01-01'
f.close()

#Now, open the file and read the content
fread = netcdf.netcdf_file('simple.nc', 'r')
print(fread.history)
time = fread.variables['time']
print(time.units)
print(time.shape)
print(time[-1])
fread.close()
