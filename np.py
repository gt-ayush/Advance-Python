import numpy as np

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

# Convert list to np.ndarray
a = np.array(a)
b = np.array(b)

print("a: ", a)
print("b: ", b)
# Checking the type of a and b
print("type of a:", type(a))
print("type of b:", type(b))

a_list = a.tolist()  # Convert np.ndarray back to list

print(a_list)
print(type(a_list))

URL = "https://www.ncei.noaa.gov/pub/data/cdo/samples/GHCND_sample_csv.csv"

raw = np.loadtxt(URL, delimiter=",", usecols=[6,7,8], skiprows=1)
print(raw)
week_one_tmax = raw[0:7, 0]
week_one_tmin = raw[0:7, 1]
week_one_prcp = raw[0:7, 2]
week_two_tmax = raw[7:14, 0]
print("Week 1 TMAX:", week_one_tmax)
print("Week 1 TMIN:", week_one_tmin)
print("Week 1 PRCP:", week_one_prcp)

# Check the size of the arrays
print("Size of Week 1 TMAX:", len(week_one_tmax))

# Alternatively, we can check the shape of the arrays
print("Size of Week 1 TMAX:", week_one_tmax.shape)

week_one_tmax = week_one_tmax / 10
week_one_tmin = week_one_tmin / 10
week_one_prcp = week_one_prcp / 10
print("Week 1 TMAX (in Celsius):", week_one_tmax)
print("Week 1 TMIN (in Celsius):", week_one_tmin)
print("Week 1 PRCP (in mm):", week_one_prcp)


week_one_trange = week_one_tmax - week_one_tmin
print("Week 1 TRANGE (in Celsius):", week_one_trange)

print("Hottest day in Week 1:", np.max(week_one_tmax))
print("Total rainfall in Week 1:", np.sum(week_one_prcp))
print("Average TMAX in Week 1:", np.mean(week_one_tmax)) # mean is the average
print("Standard deviation of TMAX in Week 1:", np.std(week_one_tmax)) # std is the standard deviation


log_prcp = np.log1p(week_one_prcp)  # log1p to avoid log(0)
print("Log-transformed PRCP:", log_prcp)

print("Week 1 precipitation is zero:", week_one_prcp == 0)
print("Type of the boolean array:", type(week_one_prcp == 0))

print("Week 1 TMIN less than -10°C:", week_one_tmin < -10)