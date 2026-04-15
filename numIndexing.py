import numpy as np


URL = "https://www.ncei.noaa.gov/pub/data/cdo/samples/GHCND_sample_csv.csv"

raw = np.loadtxt(URL, delimiter=",", usecols=[6,7,8], skiprows=1)


jan_tmax = raw[0:31, 0]
jan_tmin = raw[0:31, 1]
jan_prcp = raw[0:31, 2]

jan_tmax = jan_tmax / 10
jan_tmin = jan_tmin / 10
jan_prcp = jan_prcp / 10
print("January TMAX (in Celsius):", jan_tmax)
print("January TMIN (in Celsius):", jan_tmin)
print("January PRCP (in mm):", jan_prcp)