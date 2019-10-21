import numpy as np
from scipy.integrate import odeint
import pandas as pd

from plot_simulations_with_AUC import plot_multi_dose_delay_output
from model_simulation_plots import multi_dose_with_delay_plot

from PharmacokineticModeling.pk_model_simulations import multi_dose_sim_delay

########################################################################################################################


class MultipleDoseDelay():
    def __init__(self, model, model_parameters, number_of_compartments, number_of_dose, interval, delay=None):
        self.model = model
        self.model_parameters = model_parameters
        self.number_of_compartments = number_of_compartments
        self.number_of_dose = number_of_dose
        self.interval = interval

        if delay is None:
            delay = np.zeros(number_of_dose - 1)

        self.delay = delay

    ################

    def simulation(self, simulation_time: any, time_unit: str, dose_mg, compartment_pos=None):

        if compartment_pos is None:
            compartment_pos = [1]

        time, conc = multi_dose_sim_delay(self.model, self.model_parameters, self.number_of_compartments,
                                          simulation_time, time_unit, self.number_of_dose, self.interval, dose_mg,
                                          self.delay, compartment_pos)

        return time, conc

    ######################

    def plot_simulation(self, time, conc, figsize: tuple = (12, 6), ylabel: str = 'concentration', yunit: str = 'ng/ml',
                        auc_start: int = 0, auc_end: any = 'inf', show_auc: bool = False, show_max: bool = False):

        plot_multi_dose_delay_output(time, conc, self.number_of_dose, self.interval, self.delay, figsize, ylabel, yunit, show_max,
                               show_auc, auc_start, auc_end)

    ######################

    def multi_dose_delay_plot(self, simulation_time, time_unit: str, drug_doses, compartment_pos,
                        yunit: str = 'ng/l', figsize: tuple = (10, 6), show_hstep: bool = False):

        multi_dose_with_delay_plot(self.model, self.model_parameters, self.number_of_compartments, drug_doses, simulation_time, time_unit, self.number_of_dose,
                                   self.interval, self.delay, compartment_pos, yunit, figsize, show_hstep)

    ######################

    def model_properties(self, time, conc, t_step: any = 0.1):

        res = pd.DataFrame([time, conc], index=['Time', 'Conc']).T
        c_max = max(res['Conc']);  t_max = round(res[res['Conc'] == c_max]['Time'], 3)
        tmax = t_max.index[0] * t_step

        return print(c_max, tmax)

    ######################
