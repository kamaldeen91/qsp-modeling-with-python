import numpy as np
from scipy.integrate import odeint
import pandas as pd

from SimulationTime.simulation_time import time_for_single_dose, time_for_multi_dose, time_for_multi_dose_delay
from TwoCompartment.PK_model.two_comp_model_parameters import pk_two_comp_model_parameters
from TwoCompartment.PK_model.two_comp_model import two_comp_model

from ModelPlots.plot_simulations_with_AUC import plot_single_dose_output

from ModelPlots.model_simulation_plots import single_dose_plot


########################################################################################################################


class SingleDose():

    def __init__(self, model, model_par, simulation_time, time_unit, dose_mg, comp_num):
        self.model = model
        self.model_par = model_par
        self.simulation_time = simulation_time
        self.time_unit = time_unit
        self.dose_mg = dose_mg
        self.comp_num = comp_num

    def simulation(self, t_step: any = 0.1):
        sim_time = time_for_single_dose(self.simulation_time, self.time_unit)

        y0 = [self.dose_mg[0], 0]
        par = self.model_par()

        y = odeint(self.model, y0, sim_time, par)
        C = y[:, self.comp_num[0]]
        time = np.arange(0, len(C)) / (1 / t_step)

        return time, C

    def plot_simulation(self, time, conc, figsize: tuple = (12, 6), ylabel: any = 'Concentration', yunit: any = 'ng/mL',
                        show_max: bool=False, show_auc: bool = False, auc_start: any = 0, auc_end: any = 'inf' ):

        plot_single_dose_output(time, conc, figsize, ylabel, yunit, show_max, show_auc, auc_start, auc_end)

    def initial_cond(self):
        y0 = [self.dose_mg[0], 0]
        return len(y0)

    def single_dose_plot(self, drug_doses, compartment, yunit: str = 'ng/l', figsize: tuple = (8, 5)):

        num_comp = self.initial_cond()

        single_dose_plot(self.model, self.model_par, drug_doses, num_comp, self.simulation_time, self.time_unit,
                         compartment, yunit, figsize)

    def model_properties(self, time, conc, t_step: any = 0.1):

        res = pd.DataFrame([time, conc], index=['Time', 'Conc']).T
        c_max = max(res['Conc']);  t_max = round(res[res['Conc'] == c_max]['Time'], 3)
        tmax = t_max.index[0] * t_step

        return print(c_max, tmax)
########################################################################################################################


def two_comp_single_dose_simulation(simulation_time: any, unit: str, dose_mg, c: int = 1):

    sim_time = time_for_single_dose(simulation_time, unit)
    plt_stp = 0.1

    y0 = [dose_mg[0], 0, 0]

    par = pk_two_comp_model_parameters()

    y = odeint(two_comp_model, y0, sim_time, par)

    C = y[:, c]
    time = np.arange(0, len(C)) / (1 / plt_stp)

    return time, C


################################################################################################################################


def two_comp_multi_dose_simulation(simulation_time: any, unit: str, num_dose: int, interval, dose_mg: any, c: int = 1):

    sim_time = time_for_multi_dose(simulation_time, unit, num_dose, interval)
    plt_stp = 0.1

    y0 = [dose_mg[0], 0, 0]

    t = sim_time[0][0:]

    par = pk_two_comp_model_parameters()

    y1 = odeint(two_comp_model, y0, t, par)

    yy = y1; cconc = []; n_cc = []; nn_cc = []

    j = 1

    if len(dose_mg) == 1:

        while j < len(sim_time):
            y_n = odeint(two_comp_model, [dose_mg[0] + yy[:, 0][-1], yy[:, 1][-1], yy[:, 2][-1]], sim_time[j][1:], par)
            yy = y_n
            j += 1

            cconc.append(yy[:, c])

    else:

        while j < len(sim_time):
            y_n = odeint(two_comp_model, [dose_mg[j] + yy[:, 0][-1], yy[:, 1][-1], yy[:, 2][-1]], sim_time[j][1:], par)
            yy = y_n
            j += 1

            cconc.append(yy[:, c])

    for i in range(len(cconc)):
        n_cc.append(list(cconc[i]))
        nn_cc += n_cc[i]

    C = np.concatenate([y1[:, c], nn_cc])
    time = np.arange(0, len(C)) / (1 / plt_stp)

    return time, C


########################################################################################################################

def two_comp_multi_dose_with_delay_simulation(simulation_time: any, unit: str, num_dose: int, interval, dose_mg, delay, c: int = 1):

    a = time_for_multi_dose_delay(simulation_time, unit, num_dose, interval, delay)
    plt_stp = 0.1

    if num_dose - 1 != len(delay):
        raise Exception("Please pass in a delay array one item less/more than number of dose .\n")

    y0 = [dose_mg[0], 0, 0]
    t = np.concatenate([a[0][0:], a[1][1:int(delay[0] / plt_stp) + 1]])

    par = pk_two_comp_model_parameters()

    y1 = odeint(two_comp_model, y0, t, par)
    yy = y1; cconc = []; n_cc = []; nn_cc = []

    i = 1; new_time = []

    while i < len(delay):
        new_a = np.concatenate([a[i][int(delay[i - 1] / plt_stp) + 1:], a[i + 1][1:int(delay[i] / plt_stp) + 1]])

        new_time.append(new_a)
        i += 1

    new_time.append(a[-1][int(delay[-1] / plt_stp) + 1:])

    j = 0

    if len(dose_mg) == 1:

        while j < len(delay):
            y_n = odeint(two_comp_model, [dose_mg[0] + yy[:, 0][-1], yy[:, 1][-1], yy[:, 2][-1]], new_time[j][0:], par)
            yy = y_n
            j += 1

            cconc.append(yy[:, c])

    else:

        while j < len(delay):
            y_n = odeint(two_comp_model, [dose_mg[j + 1] + yy[:, 0][-1], yy[:, 1][-1], yy[:, 2][-1]], new_time[j][0:],
                         par)
            yy = y_n
            j += 1

            cconc.append(yy[:, c])

    for i in range(len(cconc)):
        n_cc.append(list(cconc[i]))
        nn_cc += n_cc[i]

    C = np.concatenate([y1[:, c], nn_cc])
    time = np.arange(0, len(C)) / (1 / plt_stp)

    return time, C
