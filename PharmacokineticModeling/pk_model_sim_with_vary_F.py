import numpy as np

from scipy.integrate import odeint
from simulation_time import time_for_multi_dose, time_for_multi_dose_delay


def multi_dose_simulation_vary_bioav(model, parameters_no_bioav, number_of_comp, simulation_time, time_unit, num_dose,
                                     interval, dose_mg, F, compartment_pos, plt_stp: float = 0.1):

    sim_time = time_for_multi_dose(simulation_time, time_unit, num_dose, interval)

    y0 = np.concatenate([[dose_mg[0]], np.zeros(number_of_comp - 1)])
    t = sim_time[0][0:]

    new_par = []

    if callable(parameters_no_bioav):
        for i in range(len(np.array(F))):
            par = tuple(np.concatenate([parameters_no_bioav(), [F[i]]]))
            new_par.append(par)
    else:
        for i in range(len(np.array(F))):
            par = tuple(np.concatenate([parameters_no_bioav, [F[i]]]))
            new_par.append(par)

    y1 = odeint(model, y0, t, new_par[0])

    j = 1
    yy = y1; cconc = []; n_cc = []; nn_cc = []
    if len(dose_mg) == 1:
        while j < len(sim_time):

            init_i = [yy[:, i][-1] for i in range(1, number_of_comp)]
            y_n = odeint(model, np.concatenate([[dose_mg[0] + yy[:, 0][-1]], init_i]), sim_time[j][1:], new_par[j])
            yy = y_n
            j += 1
            cconc.append(yy[:, compartment_pos[0]])
    else:
        while j < len(sim_time):
            init_i = [yy[:, i][-1] for i in range(1, number_of_comp)]
            y_n = odeint(model, np.concatenate([[dose_mg[j] + yy[:, 0][-1]], init_i]), sim_time[j][1:], new_par[j])
            yy = y_n
            j += 1
            cconc.append(yy[:, compartment_pos[0]])

    for i in range(len(cconc)):
        n_cc.append(list(cconc[i]))
        nn_cc += n_cc[i]

    C = np.concatenate([y1[:, compartment_pos[0]], nn_cc])
    time = np.arange(0, len(C)) / (1 / plt_stp)

    return time, C


def multi_dose_delay_simulation_vary_bioav(model, parameters_no_bioav, number_of_comp, simulation_time, time_unit, num_dose, interval, dose_mg,
             delay, F, compartment_pos, plt_stp: float = 0.1):

    sim_time = time_for_multi_dose_delay(simulation_time, time_unit, num_dose, interval, delay)

    if num_dose - 1 != len(delay):
        print('Error: please enter time delays')

    y0 = np.concatenate([[dose_mg[0]], np.zeros(number_of_comp - 1)])
    t = np.concatenate([sim_time[0][0:], sim_time[1][1:int(delay[0] / plt_stp) + 1]])

    new_par = []

    if callable(parameters_no_bioav):
        for i in range(len(np.array(F))):
            par = tuple(np.concatenate([parameters_no_bioav(), [F[i]]]))
            new_par.append(par)
    else:
        for i in range(len(np.array(F))):
            par = tuple(np.concatenate([parameters_no_bioav, [F[i]]]))
            new_par.append(par)

    y1 = odeint(model, y0, t, new_par[0])

    i = 1; new_time = []
    while i < len(delay):
        new_a = np.concatenate([sim_time[i][int(delay[i - 1] / plt_stp) + 1:], sim_time[i + 1][1:int(delay[i] / plt_stp) + 1]])
        new_time.append(new_a)
        i += 1

    new_time.append(sim_time[-1][int(delay[-1] / plt_stp) + 1:])

    j = 0
    yy = y1; cconc = []; n_cc = []; nn_cc = []

    if len(dose_mg) == 1:
        while j < len(delay):
            init_i = [yy[:, i][-1] for i in range(1, number_of_comp)]
            y_n = odeint(model, np.concatenate([[dose_mg[0] + yy[:, 0][-1]], init_i]), new_time[j][0:], new_par[j + 1])
            yy = y_n
            j += 1
            cconc.append(yy[:, compartment_pos[0]])
    else:
        while j < len(delay):
            init_i = [yy[:, i][-1] for i in range(1, number_of_comp)]
            y_n = odeint(model, np.concatenate([[dose_mg[j + 1] + yy[:, 0][-1]], init_i]), new_time[j][0:], new_par[j + 1])
            yy = y_n
            j += 1
            cconc.append(yy[:, compartment_pos[0]])

    for i in range(len(cconc)):
        n_cc.append(list(cconc[i]))
        nn_cc += n_cc[i]

    C = np.concatenate([y1[:, compartment_pos[0]], nn_cc])
    time = np.arange(0, len(C)) / (1 / plt_stp)

    return time, C