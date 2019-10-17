import numpy as np
from scipy.integrate import odeint
import pandas as pd
import matplotlib.pyplot as plt

from simulation_time import time_for_multi_dose
from plot_simulations_with_AUC import plot_multi_dose_output
from model_simulation_plots import multi_dose_plot

########################################################################################################################


class MultipleDose():
    def __init__(self, model, model_parameters, number_of_compartments, number_of_dose, interval):
        self.model = model
        self.model_parameters = model_parameters
        self.number_of_compartments = number_of_compartments
        self.number_of_dose = number_of_dose
        self.interval = interval

    ######################

    def time_for_multi_dose(self, num, unit: str, num_dose, interval, plt_stp: float = 0.1):

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
                    time.append(k[i * 1 * position: ((i + 1) * position) + 1])
            i += 1

        for position, item in enumerate(k):
            if time[-1][-1] != end and item == interval_end:
                time.append(k[position:])

        return time

    ################

    def multi_dose_simulation(self, simulation_time, time_unit, dose_mg, compartment_pos=None, t_step: float = 0.1):
        if compartment_pos is None:
            compartment_pos = [1]

        sim_time = self.time_for_multi_dose(simulation_time, time_unit, self.number_of_dose, self.interval)
        y0 = np.concatenate([[dose_mg[0]], np.zeros(self.number_of_compartments - 1)])
        t = sim_time[0][0:]

        if type(self.model_parameters()) != tuple:
            par = tuple([self.model_parameters()])
        else:
            par = self.model_parameters()

        y = odeint(self.model, y0, t, par)
        yy = y; cconc = []; n_cc = []; nn_cc = []
        j = 1
        if len(dose_mg) == 1:

            while j < len(sim_time):
                init_i = [yy[:, i][-1] for i in range(1, self.number_of_compartments)]
                y_n = odeint(self.model, np.concatenate([[dose_mg[0] + yy[:, 0][-1]], init_i]), sim_time[j][1:], par)
                yy = y_n
                j += 1
                cconc.append(yy[:, compartment_pos[0]])
        else:

            while j < len(sim_time):
                init_i = [yy[:, i][-1] for i in range(1, self.number_of_compartments)]
                y_n = odeint(self.model, np.concatenate([[dose_mg[j] + yy[:, 0][-1]], init_i]), sim_time[j][2:], par)
                yy = y_n
                j += 1
                cconc.append(yy[:, compartment_pos[0]])

        for i in range(len(cconc)):
            n_cc.append(list(cconc[i]))
            nn_cc += n_cc[i]

        C = np.concatenate([y[:, compartment_pos[0]], nn_cc])
        time = np.arange(0, len(C)) / (1 / t_step)

        return time, C

    ######################

    def plot_simulation(self, time, conc, figsize: tuple = (12, 6), ylabel: str = 'concentration', yunit: str = 'ng/ml',
                        auc_start: int = 0, auc_end: any = 'inf', show_auc: bool = False, show_max: bool = False):

        plot_multi_dose_output(time, conc, self.number_of_dose, self.interval, figsize, ylabel, yunit, show_max,
                               show_auc, auc_start, auc_end)

    ######################

    def multi_dose_plot(self, simulation_time, time_unit: str, drug_doses, compartment_pos,
                        yunit: str = 'ng/l', figsize: tuple = (10, 6), show_hstep: bool = False):

        multi_dose_plot(self.model, self.model_parameters, self.number_of_compartments, drug_doses,
                        simulation_time, time_unit, self.number_of_dose, self.interval, compartment_pos, yunit, figsize, show_hstep)

    ######################

    def model_properties(self, time, conc, t_step: any = 0.1):

        res = pd.DataFrame([time, conc], index=['Time', 'Conc']).T
        c_max = max(res['Conc']);  t_max = round(res[res['Conc'] == c_max]['Time'], 3)
        tmax = t_max.index[0] * t_step

        return print(c_max, tmax)

    ######################
