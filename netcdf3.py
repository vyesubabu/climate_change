from netCDF4 import Dataset
dataset = Dataset('2026010100Z-2035123118Z.nc')


"""
print dataset.dimensions.keys()
>>>
[u'time', u'lev', u'lat', u'lon', u'chars', u'ilev', u'slat', u'slon', u'nbnd']
"""


"""
print dataset.dimensions['bnds']
>> 
<type 'netCDF4._netCDF4.Dimension'>: name = 'bnds', size = 2
"""


"""
print dataset.variables.keys()
>>>
[u'P0', u'T', u'ch4vmr', u'co2vmr', u'date', u'date_written', u'datesec', u'f11vmr', u'f12vmr', u'gw', u'hyai', u'hyam', u'hybi', u'hybm', u'ilev', u'lat', u'lev', u'lon', u'mdt', u'n2ovmr', u'nbdate', u'nbsec', u'ndbase', u'ndcur', u'nlon', u'nsbase', u'nscur', u'nsteph', u'ntrk', u'ntrm', u'ntrn', u'slat', u'slon', u'sol_tsi', u'time', u'time_bnds', u'time_written', u'w_stag', u'wnummax']
"""


"""
print dataset.variables['date']
>>>
<type 'netCDF4._netCDF4.Variable'>
int32 date(time)
    long_name: current date (YYYYMMDD)
unlimited dimensions: time
current shape = (23360,)
filling on, default _FillValue of -2147483647 used
"""


"""
print dataset.variables['time']
>>>
<type 'netCDF4._netCDF4.Variable'>
float64 time(time)
    long_name: time
    units: days since 2006-01-01 00:00:00
    calendar: noleap
    bounds: time_bnds
unlimited dimensions: time
current shape = (14600,)
filling on, default _FillValue of 9.96920996839e+36 used
"""


"""
print dataset.variables['time_bnds']
>>>
<type 'netCDF4._netCDF4.Variable'>
float64 time_bnds(time, nbnd)
    long_name: time interval endpoints
unlimited dimensions: time
current shape = (14600, 2)
filling on, default _FillValue of 9.96920996839e+36 used
"""


"""
print dataset.variables['date_written']
>>>
<type 'netCDF4._netCDF4.Variable'>
|S1 date_written(time, chars)
unlimited dimensions: time
current shape = (23360, 8)
filling on, default _FillValue of   used
"""


"""
print dataset.variables['slat']
>>>
<type 'netCDF4._netCDF4.Variable'>
float64 slat(slat)
    long_name: staggered latitude
    units: degrees_north
unlimited dimensions: 
current shape = (191,)
filling on, default _FillValue of 9.96920996839e+36 used
"""


"""
print dataset['T']
>>>
<type 'netCDF4._netCDF4.Variable'>
float32 T(time, lev, lat, lon)
    mdims: 1
    units: K
    long_name: Temperature
unlimited dimensions: time
current shape = (23360, 30, 192, 288)
filling on, default _FillValue of 9.96920996839e+36 used
"""

"""
print dataset.variables['lev']
>>>
<type 'netCDF4._netCDF4.Variable'>
float64 lev(lev)
    long_name: hybrid level at midpoints (1000*(A+B))
    units: level
    positive: down
    standard_name: atmosphere_hybrid_sigma_pressure_coordinate
    formula_terms: a: hyam b: hybm p0: P0 ps: PS
unlimited dimensions: 
current shape = (30,)
filling on, default _FillValue of 9.96920996839e+36 used
"""

"""
print dataset['time'].shape
>>
(95,)
"""


"""
print dataset['tn90pETCCDI'][:]
"""


"""
print dataset['latitude'].units
>>
degrees_north
"""


"""
print dataset['longitude'].units
>>
degrees_east
"""


""""
print dataset['date'][:]

print dataset['latitude'][:]
print dataset['longitude'][:]
"""


"""
y = dataset['tasmax'][:,15,49]
for item in y:
    print item
"""