import cdsapi

client = cdsapi.Client()

# Set some paramters
# North Atlantic region [North, West, South, East]
NORTH_ATLANTIC_REGION = [80, -90, 20, 40]

# Time period.  Here just use the satellite era
START_YEAR = 1979
END_YEAR = 2024

# Download mean sea level pressure - all months for the full time period
dataset = "reanalysis-era5-single-levels-monthly-means"

years = [str(y) for y in range(START_YEAR, END_YEAR + 1)]
months = [f"{m:02d}" for m in range(1, 13)]

request = {
    "product_type": "monthly_averaged_reanalysis",
    "variable": ["mean_sea_level_pressure"],
    "year": years,
    "month": months,
    "time": "00:00",
    "area": NORTH_ATLANTIC_REGION,
    "data_format": "netcdf",
    "download_format": "unarchived"
}

client.retrieve(dataset, request, './data.nc')