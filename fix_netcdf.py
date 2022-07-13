import xarray as xr
import numpy as np

### Open netCDF
ds = xr.open_dataset('../../../../W35_GDATA_MOVED/Shared_data/Observations/'
                     'gimms3g_AWAP_grid/nc_files/lai/joined.nc')
   
### Extract dimensions   
time = ds.time.values
lat=np.unique(ds.latitude.values.flatten())
lon=np.unique(ds.longitude.values.flatten())

### Extract variable
lai = ds['lai'].values

### Write new data array
da_lai = xr.DataArray(lai,
                      dims=['time', 'lat', 'lon'],
                      coords={'time':time,
                              'lat':lat,
                              'lon':lon})

### Convert dataarray to dataset
ds_lai = da_lai.to_dataset(name='lai')

### Select years 1982-2016 (1981 only has last six months)
ds_lai = ds_lai.sel(time=slice('1982','2016'))

### Write to netcdf
ds_lai.to_netcdf('LAI_GIMMS3g.nc',
                  encoding={'time':{'dtype':'double'},
                            'lat':{'dtype':'double'},
                            'lon':{'dtype':'double'},
                            'lai':{'dtype':'float32'}})
