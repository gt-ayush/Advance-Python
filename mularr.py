def mean_range(tmin_list, tmax_list):
    assert len(tmin_list) == len(tmax_list) # Return an error if the lengths of the lists are not the same
    
    trange_list = []
    for tmin, tmax in zip(tmin_list, tmax_list):
        trange = tmax - tmin
        trange_list.append(trange)

    return sum(trange_list) / len(trange_list)

week_one_trange_list_mean = mean_range(week_one_tmin_list, week_one_tmax_list)
print("Average range of temperature in Week 1:", week_one_trange_list_mean)