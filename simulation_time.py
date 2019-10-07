import numpy as np


def time_for_single_dose(days):

    start = 0
    end = 24*days
    plt_stp = 0.1

    time = np.arange(start, end + plt_stp, plt_stp)

    return time


def time_for_multi_dose(days, num_dose, interval):

    start = 0
    end = 24*days
    plt_stp = 0.1

    k = np.arange(start, end + plt_stp, plt_stp)

    interval_end = interval * num_dose

    i = 0
    a = []

    while i < num_dose-1:
        for position, item in enumerate(k):
            if item == interval:
                a.append(k[i*1*position: ((i+1)*position)+1])
        i += 1

    for position, item in enumerate(k):
        if a[-1][-1] != end and item == interval_end:
            a.append(k[position: ])

    return a


def time_for_multi_dose_delay(days, num_dose, interval, delay):

    start = 0
    end = 24*days
    plt_stp = 0.1

    if num_dose - 1 != len(delay):

        print('Error: please enter time delays')

    else:
        k = np.arange(start, end + plt_stp, plt_stp)

        interval_end = interval * num_dose

        i = 0
        a = []

        while i < num_dose-1:
            for position, item in enumerate(k):
                if item == interval:
                    a.append(k[i*1*position: ((i+1)*position)+1])
            i += 1

        for position, item in enumerate(k):
            if a[-1][-1] != end and item == interval_end:
                a.append(k[position: ])

        return a
