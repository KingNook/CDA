import earthkit.data as ekd

# Note that only the timestep and variable visualised in
# the viewer are included in the request below.
# Data is available in both GRIB (default) and NetCDF formats;
# include 'data_format' in the request to specify a format.

data = ekd.from_source(
    'cds',
    'reanalysis-era5-single-levels-monthly-means',
    {
        'product_type': 'monthly_averaged_reanalysis',
        'variable': '2m_temperature',
        'year': '2025',
        'month': '12',
        'time': '00:00',
    }
)

data.save('2m_temperature-202512.grib')