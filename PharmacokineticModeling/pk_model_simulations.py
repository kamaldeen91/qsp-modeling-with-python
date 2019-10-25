import numpy as np

from scipy.integrate import odeint

from SimulationTime.simulation_time import time_for_single_dose, time_for_multi_dose, time_for_multi_dose_delay


def single_dose_simulation(model, model_parameters, number_of_comp, simulation_time: any, time_unit: str, dose_mg,
                           compartment_pos, plt_stp: float = 0.1):

    sim_time = time_for_single_dose(simulation_time, time_unit)
    y0 = np.concatenate([[dose_mg[0]], np.zeros(number_of_comp - 1)])

    # if callable(model_parameters):
    #     par = model_parameters()
    # else:
    #     par = tuple(model_parameters)

    if not callable(model_parameters) and len(model_parameters) == 1:
        par = tuple(model_parameters)
    else:
        if callable(model_parameters):
            par = model_parameters()
        else:
            par = tuple(model_parameters)

    y = odeint(model, y0, sim_time, par)
    conc = y[:, compartment_pos[0]]
    time = np.arange(0, len(conc)) / (1 / plt_stp)

    return time, conc

########################################################################################################################


def multi_dose_simulation(model, model_parameters, number_of_comp, simulation_time: any, time_unit: str, num_dose: int,
                          interval: any, dose_mg, compartment_pos, plt_stp: float = 0.1):

    sim_time = time_for_multi_dose(simulation_time, time_unit, num_dose, interval)
    y0 = np.concatenate([[dose_mg[0]], np.zeros(number_of_comp - 1)])
    t = sim_time[0][0:]

    if not callable(model_parameters) and len(model_parameters) == 1:
        par = tuple([model_parameters])
    else:
        if callable(model_parameters):
            par = model_parameters()
        else:
            par = tuple(model_parameters)

    y = odeint(model, y0, t, par)
    yy = y; cconc = []; n_cc = []; nn_cc = []

    j = 1

    if len(dose_mg) == 1:
        while j < len(sim_time):
            init_i = [yy[:, i][-1] for i in range(1, number_of_comp)]

            y_n = odeint(model, np.concatenate([[dose_mg[0] + yy[:, 0][-1]], init_i]), sim_time[j][1:], par)
            yy = y_n
            j += 1

            cconc.append(yy[:, compartment_pos[0]])

    else:
        while j < len(sim_time):
            init_i = [yy[:, i][-1] for i in range(1, number_of_comp)]

            y_n = odeint(model, np.concatenate([[dose_mg[j] + yy[:, 0][-1]], init_i]), sim_time[j][1:], par)
            yy = y_n
            j += 1

            cconc.append(yy[:, compartment_pos[0]])

    for i in range(len(cconc)):
        n_cc.append(list(cconc[i]))
        nn_cc += n_cc[i]

    C = np.concatenate([y[:, compartment_pos[0]], nn_cc])
    time = np.arange(0, len(C)) / (1 / plt_stp)

    return time, C


########################################################################################################################

def multi_dose_sim_delay(model, model_parameters, number_of_comp, simulation_time: any, time_unit: str, num_dose: int,
                         interval, dose_mg, delay, compartment_pos, plt_stp: float = 0.1):

    sim_time = time_for_multi_dose_delay(simulation_time, time_unit, num_dose, interval, delay)

    if num_dose - 1 != len(delay):
        raise Exception("Please pass in a delay array one item less/more than number of dose .\n")

    y0 = np.concatenate([[dose_mg[0]], np.zeros(number_of_comp - 1)])
    t = np.concatenate([sim_time[0][0:], sim_time[1][1:int(delay[0] / plt_stp) + 1]])

    if not callable(model_parameters) and len(model_parameters) == 1:
        par = tuple([model_parameters])
    else:
        if callable(model_parameters):
            par = model_parameters()
        else:
            par = tuple(model_parameters)

    # if callable(model_parameters):
    #     par = model_parameters()
    # else:
    #     par = tuple(model_parameters)

    y = odeint(model, y0, t, par)

    i = 1; new_time = []

    while i < len(delay):
        new_a = np.concatenate([sim_time[i][int(delay[i - 1] / plt_stp) + 1:], sim_time[i + 1][1:int(delay[i] / plt_stp) + 1]])
        new_time.append(new_a)
        i += 1

    new_time.append(sim_time[-1][int(delay[-1] / plt_stp) + 1:])

    j = 0
    yy = y; cconc = []; n_cc = []; nn_cc = []

    if len(dose_mg) == 1:
        while j < len(delay):
            init_i = [yy[:, i][-1] for i in range(1, number_of_comp)]

            y_n = odeint(model, np.concatenate([[dose_mg[0] + yy[:, 0][-1]], init_i]), new_time[j][0:], par)
            yy = y_n
            j += 1

            cconc.append(yy[:, compartment_pos[0]])

    else:

        while j < len(delay):
            init_i = [yy[:, i][-1] for i in range(1, number_of_comp)]

            y_n = odeint(model, np.concatenate([[dose_mg[j+1] + yy[:, 0][-1]], init_i]), new_time[j][0:], par)
            yy = y_n
            j += 1

            cconc.append(yy[:, compartment_pos[0]])

    for i in range(len(cconc)):
        n_cc.append(list(cconc[i]))
        nn_cc += n_cc[i]

    C = np.concatenate([y[:, compartment_pos[0]], nn_cc])
    time = np.arange(0, len(C)) / (1 / plt_stp)

    return time, C
