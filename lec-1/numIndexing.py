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

print("First day of January TMAX:", jan_tmax[0])
print("Last day of January TMAX:", jan_tmax[-1])
print("Last day of January TMIN:", jan_tmin[-1])
print("Last day of January PRCP:", jan_prcp[-1])

print("January TMAX every week (in order):", jan_tmax[[0, 7, 14, 21, 28]])
print("January TMAX every week (in random order):", jan_tmax[[7, 0, 14, 28, 21]])

tmax_week1 = jan_tmax[0:7] # [:7] also works
print("Average TMAX in Week 1:", np.mean(tmax_week1))

prcp_fri = jan_prcp[0::7] # [::7] also works
print("January PRCP on Fridays:", prcp_fri)

no_rain = jan_prcp == 0
print("TMAX on days with no rain (first 10):", jan_tmax[no_rain][:10])
print("TMIN on days with no rain (first 10):", jan_tmin[no_rain][:10])

# This will lead to wrong average
print("Average January PRCP (including missing values):", np.mean(jan_prcp))

jan_prcp_no_missing = jan_prcp[jan_prcp < 999.9]
print("Average January PRCP (excluding missing values):", np.mean(jan_prcp_no_missing))

cold_and_not_rainy = (jan_tmax < -10) & (jan_prcp == 0)
print("Number of days in January that are cold and not rainy:", np.sum(cold_and_not_rainy))

X = raw / 10
print(X[:5])

print("Shape of X:", X.shape)
print("Min of X:", np.min(X))

print("Min along axis 0 (columns):", np.min(X, axis=0))
print("Min along axis 1 (rows):", np.min(X, axis=1))