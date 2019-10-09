import numpy as np

from scipy.integrate import odeint

from simulation_time import time_for_single_dose, time_for_multi_dose, time_for_multi_dose_delay

from PharmacokineticModeling.pk_model_and_par import my_model, model_parameters


def single_dose_simulation(num_comp, n_days: int, dose_mg, c: int = 1):

    sim_time = time_for_single_dose(n_days)
    plt_stp = 0.1

    y0 = np.concatenate([[dose_mg], np.zeros(num_comp - 1)])

    par = model_parameters()

    y1 = odeint(my_model, y0, sim_time, par)

    C = y1[:, c]
    time = np.arange(0, len(C)) / (1 / plt_stp)

    return time, C


def multi_dose_simulation(num_comp, n_days: int, num_dose: int, interval, dose_mg, c: int = 1):

    sim_time = time_for_multi_dose(n_days, num_dose, interval)
    plt_stp = 0.1

    y0 = np.concatenate([[dose_mg[0]], np.zeros(num_comp - 1)])
    t = sim_time[0][0:]

    par = model_parameters()

    y1 = odeint(my_model, y0, t, par)
    yy = y1; cconc = []; n_cc = []; nn_cc = []

    j = 1

    while j < len(sim_time):
        init_i = [yy[:, i][-1] for i in range(1, num_comp)]

        y_n = odeint(my_model, np.concatenate([[dose_mg[j] + yy[:, 0][-1]], init_i]), sim_time[j][1:], par)
        yy = y_n
        j += 1

        cconc.append(yy[:, c])

    for i in range(len(cconc)):
        n_cc.append(list(cconc[i]))
        nn_cc += n_cc[i]

    C = np.concatenate([y1[:, c], nn_cc])
    time = np.arange(0, len(C)) / (1 / plt_stp)

    return time, C


def multi_dose_sim_delay(num_comp, n_days: int, num_dose: int, interval, dose_mg, delay, c: int = 1):

    sim_time = time_for_multi_dose_delay(n_days, num_dose, interval, delay)
    plt_stp = 0.1

    if num_dose - 1 != len(delay):
        raise Exception("Please pass in a delay array one item less/more than number of dose .\n")

    y0 = np.concatenate([[dose_mg[0]], np.zeros(num_comp - 1)])

    t = np.concatenate([sim_time[0][0:], sim_time[1][1:int(delay[0] / plt_stp) + 1]])

    par = model_parameters()

    y1 = odeint(my_model, y0, t, par)

    yy = y1; cconc = []; n_cc = []; nn_cc = []
    i = 1; new_time = []

    while i < len(delay):
        new_a = np.concatenate([sim_time[i][int(delay[i - 1] / plt_stp) + 1:], sim_time[i + 1][1:int(delay[i] / plt_stp) + 1]])

        new_time.append(new_a)
        i += 1

    new_time.append(sim_time[-1][int(delay[-1] / plt_stp) + 1:])

    j = 0
    while j < len(delay):

        init_i = [yy[:, i][-1] for i in range(1, num_comp)]

        y_n = odeint(my_model, np.concatenate([[dose_mg[j + 1] + yy[:, 0][-1]], init_i]), new_time[j][0:], par)
        yy = y_n
        j += 1

        cconc.append(yy[:, c])

    for i in range(len(cconc)):
        n_cc.append(list(cconc[i]))
        nn_cc += n_cc[i]

    C = np.concatenate([y1[:, c], nn_cc])
    time = np.arange(0, len(C)) / (1 / plt_stp)

    return time, C
