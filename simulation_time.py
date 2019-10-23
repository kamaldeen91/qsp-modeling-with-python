import numpy as np


def time_for_single_dose(num, unit: str, plt_stp: float = 0.1):
    if unit == 'day' or unit == 'days' or unit == 'Day' or unit == 'Days':
        end = 24*num

    else:
        end = num
    time = np.arange(0, end + plt_stp, plt_stp)

    return time

##########################################################################


def time_for_multi_dose(num, unit: str, num_dose, interval, plt_stp: float = 0.1):

    if unit == 'day' or unit == 'days' or unit == 'Day' or unit == 'Days':
        end = 24 * num
    else:
        end = num

    k = np.arange(0, end + plt_stp, plt_stp)
    interval_end = interval * (num_dose - 1)

    i = 0
    time = []

    while i < num_dose - 1:
        for position, item in enumerate(k):
            if item == interval:
                time.append(k[i*1*position: ((i+1)*position)+1])
        i += 1

    for position, item in enumerate(k):
        if time[-1][-1] != end and item == interval_end:
            time.append(k[position: ])

    return time

##########################################################################


def time_for_multi_dose_delay(num, unit: str, num_dose, interval, delay, plt_stp: float = 0.1):

    if num_dose - 1 != len(delay):
        raise Exception("You have to pass in  delay in simulation starting from second dose).\n")

    if unit == 'day' or unit == 'days' or unit == 'Day' or unit == 'Days':
        end = 24 * num
    else:
        end = num

    k = np.arange(0, end + plt_stp, plt_stp)
    interval_end = interval * (num_dose - 1)

    i = 0
    time = []

    while i < num_dose - 1:
        for position, item in enumerate(k):
            if item == interval:
                time.append(k[i*1*position: ((i+1)*position)+1])
        i += 1

    for position, item in enumerate(k):
        if time[-1][-1] != end and item == interval_end:
            time.append(k[position: ])

    return time
